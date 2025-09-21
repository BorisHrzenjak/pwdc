# PWDC - Print Working Directory Copy

A simple command-line utility that copies the current working directory path to your clipboard.

## Description

PWDC is a lightweight Python script that gets the absolute path of your current working directory and automatically copies it to your clipboard. Perfect for when you need to quickly grab the current folder path for use in other applications.

## Features

- 🚀 **Fast**: Instantly copies current directory path to clipboard
- 📋 **Clipboard Integration**: Uses `pyperclip` for reliable clipboard operations
- 💻 **Cross-Platform**: Works on Windows, macOS, and Linux
- 🔧 **Simple**: No configuration required

## Installation

### Prerequisites

- Python 3.6 or higher
- `pyperclip` library

### Setup

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install pyperclip
   ```

### Platform-Specific Setup

#### Windows
The included `pwdc.bat` file allows you to run the command from anywhere:

1. The batch file automatically detects your username using `%USERNAME%`, so no path modification is needed if you place the files in `C:\Users\[YourUsername]\Scripts\pwdc\`
2. Add the directory containing `pwdc.bat` to your system PATH
3. Or copy `pwdc.bat` to a directory that's already in your PATH

**Note**: If you place the files in a different location, update the path in `pwdc.bat` accordingly.

#### Linux/macOS
The included `pwdc` shell script allows you to run the command from anywhere:

1. Make the script executable:
   ```bash
   chmod +x pwdc
   ```
2. Add the directory containing `pwdc` to your PATH, or copy it to a directory already in your PATH (like `/usr/local/bin/`)
   ```bash
   # Option 1: Add to PATH (add this to your ~/.bashrc or ~/.zshrc)
   export PATH="$PATH:/path/to/your/pwdc/directory"
   
   # Option 2: Copy to system directory
   sudo cp pwdc /usr/local/bin/
   ```

## Usage

### Direct Python execution:
```bash
# Windows
python pwdc.py

# Linux/macOS
python3 pwdc.py
```

### Using wrapper scripts:
```bash
# Windows (using batch file)
pwdc

# Linux/macOS (using shell script)
pwdc
```

After running the command, the current directory path will be copied to your clipboard and you'll see:
```
Path copied to clipboard!
```

## Example

```bash
C:\Users\Boris\Documents\MyProject> pwdc
Path copied to clipboard!
```

The clipboard will now contain: `C:\Users\Boris\Documents\MyProject`

## Files

- `pwdc.py` - Main Python script
- `pwdc.bat` - Windows batch file wrapper for easy execution
- `pwdc` - Linux/macOS shell script wrapper for easy execution
- `requirements.txt` - Python dependencies
- `.gitignore` - Git ignore rules

## Dependencies

- `pathlib` (built-in Python module)
- `pyperclip` - For clipboard operations

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.
