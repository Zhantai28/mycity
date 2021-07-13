from django.db import models
from django.db.models.fields import NullBooleanField, TextField


class Proposal(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="proposal", null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
