from django.db import models


"""Application models for storing blog entries."""


class Blog(models.Model):
    """A single blog post."""

    title = models.CharField(max_length=100, unique=True)
    text = models.TextField(unique=True)
    code = models.TextField(unique=True)

    def __str__(self):
        return self.title

    
