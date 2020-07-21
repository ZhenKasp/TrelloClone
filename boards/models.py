from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def return_id(self):
        return self.id

class Card(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    name = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.name
