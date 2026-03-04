from models.models import User, Project, Task

def run_tests():
    print("Starting simple tests...")

    # 1. Test if User class works
    u = User("TestUser", "test@mail.com", 1)
    if u.name == "TestUser" and u.id == 1:
        print("[PASS] User creation works")
    else:
        print("[FAIL] User creation failed")

    # 2. Test if Project class works
    p = Project("TestProj", "TestUser", 1)
    if p.title == "TestProj":
        print("[PASS] Project creation works")
    else:
        print("[FAIL] Project creation failed")

    # 3. Test if Task status starts as Incomplete
    t = Task("TestTask", 1, 1)
    if t.status == "Incomplete":
        print("[PASS] Task status works")
    else:
        print("[FAIL] Task status failed")

if __name__ == "__main__":
    run_tests()