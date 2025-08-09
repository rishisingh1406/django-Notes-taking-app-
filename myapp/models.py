from django.db import models

class Notes(models.Model):
    topic = models.CharField(max_length=200)
    ID =models.ImageField(max_length=1000)
    message = models.TextField(max_length=10000)

    def __str__(self):
        return self.topic 