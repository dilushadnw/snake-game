# Snake Game 🐍

A classic Snake game implementation for Windows 10/11 with a professional installer that auto-launches after installation.

![Snake Game](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%2010%2F11-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎮 Game Features

- **Classic Gameplay**: Control the snake, eat food, and grow longer
- **Smooth Controls**: Responsive arrow key controls
- **Score Tracking**: Real-time score display
- **Game Over Detection**: Collision detection with walls and self
- **Easy Restart**: Press SPACE or ENTER to restart after game over
- **Clean Interface**: 600x600 pixel window with colorful graphics
- **Grid-based Movement**: 20x20 cell grid for smooth gameplay

## 🎯 How to Play

### Controls
- **↑ Up Arrow**: Move up
- **↓ Down Arrow**: Move down
- **← Left Arrow**: Move left
- **→ Right Arrow**: Move right
- **SPACE/ENTER**: Restart game after game over

### Objective
- Control the snake to eat red food items
- Each food item increases your score by 1
- The snake grows longer with each food eaten
- Avoid hitting the walls or the snake's own body
- Try to achieve the highest score possible!

### Game Rules
- The snake moves continuously in the current direction
- You cannot make 180-degree turns (e.g., if moving right, cannot immediately move left)
- The game ends when the snake hits a wall or itself
- Food spawns randomly on the grid after being eaten

## 💻 For Players - Installation & Running

### Option 1: Download and Install (Recommended)

1. **Download the Installer**
   - Download `SnakeGameInstaller.exe` from the releases page
   - No Python installation required!

2. **Run the Installer**
   - Double-click `SnakeGameInstaller.exe`
   - Follow the installation wizard
   - Choose installation directory (default: `C:\Program Files\Snake Game`)
   - Select whether to create a desktop shortcut

3. **Auto-Launch**
   - The game will automatically launch after installation completes
   - If you chose not to launch immediately, find the game in:
     - Desktop shortcut (if created)
     - Start Menu → Snake Game
     - Installation directory

### Option 2: Run Standalone Executable

1. **Download** `snake_game.exe` from the releases
2. **Double-click** to run - no installation needed!

### Uninstalling

- **Windows 10**: Settings → Apps → Snake Game → Uninstall
- **Windows 11**: Settings → Apps → Installed apps → Snake Game → Uninstall
- **Alternative**: Start Menu → Snake Game → Uninstall Snake Game

## 🛠️ For Developers - Setup & Building

### Prerequisites

- **Python**: Version 3.8 or higher
  - Download from [python.org](https://www.python.org/downloads/)
  - Make sure to check "Add Python to PATH" during installation
- **pip**: Python package installer (included with Python)
- **Inno Setup**: For creating the Windows installer
  - Download from [jrsoftware.org](https://jrsoftware.org/isdl.php)
  - Only needed if you want to create the installer

### Running from Source

1. **Clone the Repository**
   ```bash
   git clone https://github.com/dilushadnw/snake-game.git
   cd snake-game
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Game**
   ```bash
   python snake_game.py
   ```

### Building the Executable

#### Step 1: Build the .exe with PyInstaller

**Windows Command Line:**
```bash
build_exe.bat
```

**Or manually:**
```bash
# Install dependencies
pip install -r requirements.txt

# Install PyInstaller
pip install pyinstaller

# Build the executable
pyinstaller snake_game.spec
```

The executable will be created in the `dist` folder as `snake_game.exe`.

#### Step 2: Create the Windows Installer

1. **Install Inno Setup**
   - Download from [jrsoftware.org/isdl.php](https://jrsoftware.org/isdl.php)
   - Run the installer and follow the setup wizard

2. **Build the Installer**
   - Open Inno Setup Compiler
   - Click File → Open and select `installer.iss`
   - Click Build → Compile (or press Ctrl+F9)
   - The installer will be created in the `Output` folder as `SnakeGameInstaller.exe`

**Alternative (Command Line):**
```bash
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss
```

### Project Structure

```
snake-game/
├── snake_game.py          # Main game source code
├── requirements.txt       # Python dependencies (pygame)
├── build_exe.bat         # Windows batch script to build .exe
├── snake_game.spec       # PyInstaller spec file configuration
├── installer.iss         # Inno Setup script
├── README.md             # This file
├── .gitignore           # Git ignore file
├── build/               # PyInstaller build directory (ignored)
├── dist/                # Output directory for .exe (ignored)
└── Output/              # Inno Setup output directory (ignored)
```

### Build Configuration Details

#### PyInstaller Configuration (`snake_game.spec`)
- **Single file**: All dependencies bundled into one .exe
- **Windowed mode**: No console window (console=False)
- **UPX compression**: Reduces file size
- **Target architecture**: 64-bit compatible

#### Inno Setup Configuration (`installer.iss`)
- **Auto-launch**: Game launches after installation (postinstall flag)
- **Desktop shortcut**: Optional desktop icon
- **Start Menu entry**: Automatically created
- **Uninstaller**: Proper uninstall through Windows Settings
- **Privilege level**: Lowest required (user install)
- **Architecture**: 64-bit compatible

## 📋 System Requirements

### For Players
- **Operating System**: Windows 10 or Windows 11
- **Architecture**: 64-bit (x64)
- **Disk Space**: ~50 MB
- **Display**: 800x600 minimum resolution

### For Developers
- **Python**: 3.8 or higher
- **Pygame**: 2.5.0 or higher (automatically installed via requirements.txt)
- **PyInstaller**: Latest version (for building .exe)
- **Inno Setup**: 6.0 or higher (for creating installer)

## 🎨 Technical Specifications

- **Window Size**: 600x600 pixels
- **Grid Size**: 20x20 cells
- **Cell Size**: 30x30 pixels
- **Frame Rate**: 10 FPS
- **Starting Snake Length**: 3 segments
- **Colors**:
  - Background: Black
  - Snake: Green (head) / Dark Green (body)
  - Food: Red
  - Text: White
  - Instructions: Gray

## 🐛 Troubleshooting

### Game won't start after installation
- Check if Windows Defender or antivirus blocked the executable
- Try running as administrator
- Reinstall the game

### Build errors when creating .exe
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Update PyInstaller: `pip install --upgrade pyinstaller`
- Delete `build` and `dist` folders and rebuild

### Installer creation fails
- Verify Inno Setup is properly installed
- Make sure `snake_game.exe` exists in the `dist` folder
- Check that paths in `installer.iss` are correct

## 📝 Development Notes

### Code Structure
- **Snake class**: Manages snake movement, growth, and collision detection
- **Food class**: Handles food positioning and respawning
- **Game class**: Main game loop, event handling, rendering, and state management

### Key Features Implementation
- **Collision Detection**: Checks both wall and self-collision
- **Direction Control**: Prevents 180-degree turns for realistic gameplay
- **Food Spawning**: Ensures food doesn't spawn on snake's body
- **Game Over State**: Allows easy restart without closing the window

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created for Windows 10/11 desktop gaming.

## 🎯 Future Enhancements (Ideas)

- High score tracking (persistent storage)
- Difficulty levels (speed adjustment)
- Sound effects and background music
- Multiple snake skins/themes
- Obstacles and power-ups
- Multiplayer mode
- Leaderboard system

---

**Enjoy the game! 🐍🎮**
