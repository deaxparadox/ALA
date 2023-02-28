from django.db import models

class URLS(models.Model):
    visited = models.URLField(unique=True)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.visited