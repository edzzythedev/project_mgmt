import argparse
from models.models import User, Project, Task
from utils.database import load_db, save_db
from tabulate import tabulate # External package for Excelled grade

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Command: add-user
    u_parser = subparsers.add_parser("add-user")
    u_parser.add_argument("--name", required=True)
    u_parser.add_argument("--email", required=True)

    # Command: add-project
    p_parser = subparsers.add_parser("add-project")
    p_parser.add_argument("--title", required=True)
    p_parser.add_argument("--owner", required=True)

    # Command: list-all
    subparsers.add_parser("list")

    args = parser.parse_args()
    data = load_db()

    if args.command == "add-user":
        new_id = len(data["users"]) + 1
        new_user = User(args.name, args.email, new_id)
        data["users"].append(vars(new_user))
        save_db(data)
        print(f"User {args.name} added!")

    elif args.command == "add-project":
        new_id = len(data["projects"]) + 1
        new_proj = Project(args.title, args.owner, new_id)
        data["projects"].append(vars(new_proj))
        save_db(data)
        print(f"Project {args.title} added!")

    elif args.command == "list":
        print("\n--- USERS ---")
        print(tabulate(data["users"], headers="keys", tablefmt="grid"))
        print("\n--- PROJECTS ---")
        print(tabulate(data["projects"], headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()