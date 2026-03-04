import argparse
from models.models import User, Project, Task
from utils.database import load_db, save_db
from tabulate import tabulate

def main():
    # 1. Setup Argparse
    parser = argparse.ArgumentParser(description="My Management Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Command: add-user
    u_p = subparsers.add_parser("add-user")
    u_p.add_argument("--name", required=True)
    u_p.add_argument("--email", required=True)

    # Command: add-project
    p_p = subparsers.add_parser("add-project")
    p_p.add_argument("--title", required=True)
    p_p.add_argument("--owner", required=True)

    # Command: add-task
    t_p = subparsers.add_parser("add-task")
    t_p.add_argument("--title", required=True)
    t_p.add_argument("--project_id", required=True)

    # Command: list
    subparsers.add_parser("list")

    # 2. Parse arguments and load data
    args = parser.parse_args()
    db = load_db()

    # 3. Logic for each command
    if args.command == "add-user":
        new_id = len(db["users"]) + 1
        u = User(args.name, args.email, new_id)
        # Manually making a dictionary for JSON
        db["users"].append({
            "id": u.id, 
            "name": u.name, 
            "email": u.email, 
            "date": u.created_at
        })
        save_db(db)
        print(f"Added user: {u.name}")

    elif args.command == "add-project":
        new_id = len(db["projects"]) + 1
        p = Project(args.title, args.owner, new_id)
        db["projects"].append({
            "id": p.id, 
            "title": p.title, 
            "owner": p.owner
        })
        save_db(db)
        print(f"Added project: {p.title}")

    elif args.command == "add-task":
        new_id = len(db["tasks"]) + 1
        t = Task(args.title, args.project_id, new_id)
        db["tasks"].append({
            "id": t.id, 
            "title": t.title, 
            "project_id": t.project_id, 
            "status": t.status
        })
        save_db(db)
        print(f"Added task: {t.title}")

    elif args.command == "list":
        # Show everything using tabulate
        print("\n--- USERS ---")
        print(tabulate(db["users"], headers="keys", tablefmt="grid"))
        print("\n--- PROJECTS ---")
        print(tabulate(db["projects"], headers="keys", tablefmt="grid"))
        print("\n--- TASKS ---")
        print(tabulate(db["tasks"], headers="keys", tablefmt="grid"))

    else:
        parser.print_help()

if __name__ == "__main__":
    main()