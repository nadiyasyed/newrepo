from django.db import models
from utils import ROLE_CHOICES
from django.contrib.auth.models import User


class LogUser(User):
    firstname=models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    role= models.CharField(max_length=32,choices=ROLE_CHOICES)
    emal=models.EmailField(max_length=30,blank=True)
    paswd=models.CharField(max_length=50)

    def __string__(self):
        return self.firstname,self.lastname,self.email



