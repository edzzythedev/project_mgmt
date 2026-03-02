import unittest
from models.models import User, Project

class TestProjectManager(unittest.TestCase):
    
    def test_user_initialization(self):
        """Test if User class correctly inherits and sets attributes"""
        user = User("Test Admin", "admin@test.com", 99)
        self.assertEqual(user.name, "Test Admin")
        self.assertEqual(user.id, 99)
        self.assertEqual(user.email, "admin@test.com")

    def test_project_link(self):
        """Test if Project correctly stores owner information"""
        project = Project("Build CLI", "admin@test.com", 1)
        self.assertEqual(project.owner_email, "admin@test.com")
        self.assertEqual(project.title, "Build CLI")

if __name__ == '__main__':
    unittest.main()