from django.db import models

class Notes(models.Model):
    ID = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.topic 