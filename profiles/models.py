from django.db import models

# Create your models here.
class Users(models.Model):
    username        = models.TextField(blank=False,null=False)
    email           = models.TextField(blank=False,null=False)
    password        = models.CharField(max_length=20)

    def __str__(self):
        return self.username