from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company =  models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    skills = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
