from django.db import models


class ErrorLog(models.Model):
    status_code = models.IntegerField()
    error = models.TextField()

    def __str__(self):
        return f"{self.status_code}: {self.error[:50]}..."
