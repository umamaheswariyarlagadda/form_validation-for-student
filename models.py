from django.db import models

# Create your models here.
class Post(models.Model):
    MALE='M'
    FEMALE='F'
    GENDER_CHOICES=[
        (MALE,'Male'),
        (FEMALE,'Female'),
    ]
    username=models.CharField(max_length=20,blank=False,null=False)
    text=models.TextField(blank=False,null=False)
    gender=models.CharField(max_length=6,choices=GENDER_CHOICES,default=MALE)
    time=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.username
