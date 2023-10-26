from django.db import models

# Create your models here.



class UserModel(models.Model):
    username = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.username
