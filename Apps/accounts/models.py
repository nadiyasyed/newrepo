from django.db import models
from utils import ROLE_CHOICES
from django.contrib.auth.models import User


class LogUser(User):

    role= models.CharField(max_length=32,choices=ROLE_CHOICES)
    
    def __string__(self):
        return self.firstname,self.lastname,self.email



