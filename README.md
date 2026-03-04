# Multi-User Project Management CLI Tool

A professional command-line interface for managing developers, projects, and tasks. Built with Python, this tool uses Object-Oriented Programming (OOP) principles and persistent JSON storage.

## Features
- **User Management**: Create and list team members.
- **Project Tracking**: Assign projects to specific users (One-to-Many).
- **Task Management**: Assign tasks to projects.
- **Data Persistence**: All data is saved locally in JSON format.
- **Professional UI**: Tabular data display using the `tabulate` library.

## Project Structure
- `main.py`: The CLI entry point and command controller.
- `models/`: Contains the logic for Users, Projects, and Tasks (Inheritance & Encapsulation).
- `utils/`: Handles File I/O and data persistence.
- `data/`: Stores the `database.json` file.
- `tests/`: Folder containing unit tests for code reliability.
- `requirements.txt`: Lists external dependencies (tabulate).

## Installation & Usage
1. Install dependencies:
   `pip install -r requirements.txt`

2. Run the tool:
   `python3 main.py --help`

3. Run tests:
   `python3 -m tests.test_logic`