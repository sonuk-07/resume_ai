from django.db import models
from resumes.models import Resume
from jobs.models import Job
# Create your models here.
class Prediction(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    predicted_role = models.CharField(max_length=100)
    confidence = models.FloatField()
    recommended_jobs = models.ManyToManyField(Job, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction: {self.predicted_role} for {self.resume.user.username}"
    

class SkillSuggestion(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    missing_skill = models.CharField(max_length=50)
    suggested_for_role = models.CharField(max_length=100)

    def __str__(self):
        return f"Suggested Skill: {self.missing_skill} for {self.suggested_for_role}"