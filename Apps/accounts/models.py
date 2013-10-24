from django.db import models

class LogUser(models.Model):
    firstname=models.CharFIeld(max_length=20)
    lastname = models.CharField(max_length=20)


