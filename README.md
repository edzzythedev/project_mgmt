# Multi-User Project Management CLI Tool

A professional command-line interface for managing developers, projects, and tasks. Built with Python, this tool uses Object-Oriented Programming (OOP) principles and persistent JSON storage.

## 🚀 Features
- **User Management**: Create and list team members.
- **Project Tracking**: Assign projects to specific users (One-to-Many).
- **Task Management**: Assign tasks to projects.
- **Data Persistence**: All data is saved locally in JSON format.
- **Professional UI**: Tabular data display using the `tabulate` library.

## 📁 Project Structure
- `main.py`: The CLI entry point and command controller.
- `models/`: Contains the logic for Users, Projects, and Tasks (Inheritance & Encapsulation).
- `utils/`: Handles File I/O and data persistence.
- `data/`: Stores the `database.json` file.
- `tests.py`: Unit tests for ensuring code reliability.

## 🛠️ Installation & Setup
1. Clone the repository to your WSL Ubuntu environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt