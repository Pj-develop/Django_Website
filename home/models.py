from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    username=models.TextField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    mobile=models.CharField(max_length=11)

    def __str__(self):
        return self.name
# Create your models here.
