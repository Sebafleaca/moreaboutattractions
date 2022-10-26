from django.db import models

class Users(models.Model):

    user_name = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user_name)
