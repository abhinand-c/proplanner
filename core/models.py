from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Role(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class User(AbstractUser):
    class RoleLevel(models.IntegerChoices):
        JR = 0, 'Junior'
        MID = 1, 'Mid'
        SR = 2, 'Senior'

    full_name = models.CharField('Full Name', max_length=150)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    role_level = models.IntegerField(choices=RoleLevel.choices, default=RoleLevel.JR)
    skills = models.ManyToManyField(Skill, blank=True)
    interests = models.ManyToManyField(Skill, blank=True, related_name="skill_interests")

    first_name = None
    last_name = None

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name
