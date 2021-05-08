from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Role(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

class Skill(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

class User(AbstractUser):
    class RoleLevel(models.IntegerChoices):
        JR = 0, 'Junior'
        MID = 1, 'Mid'
        SR = 2, 'Senior'
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    role_level = models.IntegerField(choices=RoleLevel.choices, default=RoleLevel.JR)
    skills = models.ManyToManyField(Skill, blank=True)
    interests = models.ManyToManyField(Skill, blank=True, related_name="skill_interests")
