from statistics import mode
from django.db import models
from django.forms import model_to_dict

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200)
    note = models.TextField()
    created = models.DateTimeField(auto_now_add=True)