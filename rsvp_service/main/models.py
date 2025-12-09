from django.db import models

class RSVP(models.Model):
    event_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    response = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} - {self.response}"