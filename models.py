from django.db import models

class Role(models.Model):
    ROLE_CHOISE = [
        ("admin", "Admin"),
        ("user", "User")
    ]
    name = models.CharField(max_length=20, choses=ROLE_CHOISE, unique=True)

class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete= models.CASCADE, related_name="users")