from django.db import models

# Create your models here.

class stuffs_sort(models.Model):
    name = models.CharField(max_length=225)
    category = models.IntegerField()
    image = models.CharField(max_length=225)

    def __str__(self):
        return str(self.id)