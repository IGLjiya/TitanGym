from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class LoginView(AbstractUser):
    is_trainer = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)


class Trainer(models.Model):

    typeTrianer = {
        'Personal Trainer': 'Personal Trainer',
        'Group Fitness Instructor': 'Group Fitness Instructor',
        'Strength & Conditioning Coach': 'Strength & Conditioning Coach',
        'Weightlifting & Bodybuilding Coach': 'Weightlifting & Bodybuilding Coach',
        'Cardio Trainer ': 'Cardio Trainer ',
        'Rehabilitation & Injury Recovery Trainer': 'Rehabilitation & Injury Recovery Trainer',
        'Sports-Specific Trainer': 'Sports-Specific Trainer',
        'Functional Fitness Trainer':'Functional Fitness Trainer',
        'Senior Fitness Trainer': 'Senior Fitness Trainer',
        'Yoga & Pilates Instructor': 'Yoga & Pilates Instructor',
        'Nutrition & Wellness Coach': 'Nutrition & Wellness Coach',
    }

    user = models.ForeignKey(LoginView,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phoneNo = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    proof = models.FileField(upload_to='TrainerProof/')
    type = models.CharField(max_length=100,choices=typeTrianer)

    def __str__(self):
        return self.name


class Member(models.Model):
    user = models.ForeignKey(LoginView,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phoneNo = models.CharField(max_length=50)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.name