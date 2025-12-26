"""
Snake Game - A classic Snake game implementation using Pygame
Author: Created for Windows 10/11
Controls: Arrow keys to move the snake
"""

import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
GRID_SIZE = 30  # Size of each cell in pixels (600/20 = 30)
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE  # 20 cells wide
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE  # 20 cells tall
FPS = 10

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    """Snake class to manage snake position, movement, and growth"""
    
    def __init__(self):
        """Initialize snake at center of screen with length 3"""
        center_x = GRID_WIDTH // 2
        center_y = GRID_HEIGHT // 2
        self.body = [
            (center_x, center_y),
            (center_x - 1, center_y),
            (center_x - 2, center_y)
        ]
        self.direction = RIGHT
        self.grow = False
    
    def move(self):
        """Move snake in current direction"""
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # Add new head
        self.body.insert(0, new_head)
        
        # Remove tail if not growing
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
    
    def change_direction(self, new_direction):
        """Change snake direction if not opposite to current direction"""
        # Prevent 180-degree turns
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction
    
    def eat_food(self):
        """Mark snake to grow on next move"""
        self.grow = True
    
    def check_collision(self):
        """Check if snake collided with walls or itself"""
        head_x, head_y = self.body[0]
        
        # Check wall collision
        if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
            return True
        
        # Check self collision
        if self.body[0] in self.body[1:]:
            return True
        
        return False
    
    def draw(self, surface):
        """Draw snake on the surface"""
        for i, (x, y) in enumerate(self.body):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            # Draw head slightly different
            color = GREEN if i == 0 else DARK_GREEN
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)  # Border


class Food:
    """Food class to manage food position"""
    
    def __init__(self):
        """Initialize food at random position"""
        self.position = (0, 0)
        self.randomize_position()
    
    def randomize_position(self, snake_body=None):
        """Place food at random position not occupied by snake"""
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            self.position = (x, y)
            
            # Make sure food doesn't spawn on snake
            if snake_body is None or self.position not in snake_body:
                break
    
    def draw(self, surface):
        """Draw food on the surface"""
        x, y = self.position
        rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, RED, rect)
        pygame.draw.rect(surface, BLACK, rect, 1)  # Border


class Game:
    """Main game class to manage game state and logic"""
    
    def __init__(self):
        """Initialize game window and components"""
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.reset_game()
    
    def reset_game(self):
        """Reset game to initial state"""
        self.snake = Snake()
        self.food = Food()
        self.food.randomize_position(self.snake.body)
        self.score = 0
        self.game_over = False
    
    def handle_events(self):
        """Handle keyboard and window events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    # Restart game on any key press after game over
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.reset_game()
                else:
                    # Handle direction changes
                    if event.key == pygame.K_UP:
                        self.snake.change_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction(RIGHT)
        
        return True
    
    def update(self):
        """Update game state"""
        if not self.game_over:
            # Move snake
            self.snake.move()
            
            # Check if snake ate food
            if self.snake.body[0] == self.food.position:
                self.snake.eat_food()
                self.score += 1
                self.food.randomize_position(self.snake.body)
            
            # Check for collisions
            if self.snake.check_collision():
                self.game_over = True
    
    def draw(self):
        """Draw all game elements"""
        # Clear screen
        self.screen.fill(BLACK)
        
        # Draw snake and food
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw game over screen
        if self.game_over:
            # Semi-transparent overlay
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))
            
            # Game over text
            game_over_text = self.font.render("GAME OVER!", True, RED)
            final_score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
            restart_text = self.small_font.render("Press SPACE or ENTER to restart", True, WHITE)
            
            # Center the text
            game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
            score_rect = final_score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
            
            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(final_score_text, score_rect)
            self.screen.blit(restart_text, restart_rect)
        else:
            # Draw instructions on first few frames
            if self.score == 0 and len(self.snake.body) == 3:
                instructions = self.small_font.render("Use Arrow Keys to move", True, GRAY)
                instructions_rect = instructions.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 30))
                self.screen.blit(instructions, instructions_rect)
        
        # Update display
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        running = True
        
        while running:
            # Handle events
            running = self.handle_events()
            
            # Update game state
            self.update()
            
            # Draw everything
            self.draw()
            
            # Control frame rate
            self.clock.tick(FPS)
        
        # Quit
        pygame.quit()
        sys.exit()


def main():
    """Main entry point for the game"""
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"Error running game: {e}")
        pygame.quit()
        sys.exit(1)


if __name__ == "__main__":
    main()
