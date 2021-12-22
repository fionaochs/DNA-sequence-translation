from django.db import models

# Create your models here.
class Sequence(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title

class Result(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        """A string representation of the model."""
        return self.title