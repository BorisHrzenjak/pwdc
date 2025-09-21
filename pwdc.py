#!/usr/bin/env python3

from pathlib import Path
import pyperclip

def main():
    cwd = Path(".").absolute()
    pyperclip.copy(str(cwd))
    print("Path copied to clipboard!")

if __name__ == "__main__":
    main() 
