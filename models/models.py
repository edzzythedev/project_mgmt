import datetime

# The Parent class - handles ID and Date for everyone
class BaseModel:
    def __init__(self, id_val):
        self.id = id_val
        # Just saving the date as a simple string
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d")

# User inherits from BaseModel
class User(BaseModel):
    def __init__(self, name, email, id_val):
        BaseModel.__init__(self, id_val)
        self._name = name # Underscore used for the @property rule
        self.email = email

    @property
    def name(self):
        return self._name

# Project inherits from BaseModel
class Project(BaseModel):
    def __init__(self, title, owner, id_val):
        BaseModel.__init__(self, id_val)
        self.title = title
        self.owner = owner

# Task inherits from BaseModel
class Task(BaseModel):
    def __init__(self, title, project_id, id_val):
        BaseModel.__init__(self, id_val)
        self.title = title
        self.project_id = project_id
        self.status = "Incomplete"