from django.db import models

class Role(models.Model):
    ROLE_CHOISE = [
        ("admin", "Admin"),
        ("user", "User")
    ]
    name = models.CharField(max_length=20, choices=ROLE_CHOISE, unique=True)
    def __str__(self):
        return self.get_name_display()

    
class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete= models.CASCADE, related_name="users")

    def __str__(self):
        return self.name()

class TaskStatus(models.Model):
    Status_choose = [
        ("in_process", "In process"),
        ("done", "Done"),
        ("postponed", "Postponed"),
    ]
    status_title = models.CharField(max_length=100, choices=Status_choose)

    def __str__(self):
        return self.get_status_title_display()

class Task(models.Model):
    title = models.CharField(max_length=100)
    info = models.CharField(max_length=256)
    status = models.ForeignKey(TaskStatus, on_delete= models.CASCADE)
    user_rel = models.ForeignKey(Users, on_delete= models.CASCADE)

    def __str__(self):
         return f"{self.title} ({self.status})"


