from django.db import models

class Message(models.Model):
    text = models.TextField()

    def __str__(self):
        return (self.text[:50] + '...') if len(self.text) > 50 else self.text

