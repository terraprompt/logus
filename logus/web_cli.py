#!/usr/bin/env python3
"""
Script to run the Logus web interface.
"""
import os
import sys


def main():
    """Run the Logus web interface."""
    # Add the current directory to the path so we can import logus
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

    try:
        from logus.web import app
        import uvicorn
    except ImportError as e:
        print(f"Error importing web modules: {e}")
        print("Please install with web extras: pip install logus[web]")
        sys.exit(1)

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
