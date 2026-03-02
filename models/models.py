import datetime

class BaseModel:
    """Base class for shared logic (Inheritance)"""
    def __init__(self, id_val=None):
        self.id = id_val
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class User(BaseModel):
    def __init__(self, name, email, id_val=None):
        super().__init__(id_val)
        self.name = name
        self.email = email

class Project(BaseModel):
    def __init__(self, title, owner_email, id_val=None):
        super().__init__(id_val)
        self.title = title
        self.owner_email = owner_email # One-to-Many Relationship

class Task(BaseModel):
    def __init__(self, title, project_id, id_val=None):
        super().__init__(id_val)
        self.title = title
        self.project_id = project_id # One-to-Many Relationship
        self.status = "Incomplete"

    def mark_complete(self):
        self.status = "Complete"