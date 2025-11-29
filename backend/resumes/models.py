from django.db import models 
from django.conf import settings 

class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to="resume/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    text_extracted = models.TextField(blank=True, null=True)
    predicted_role = models.CharField(max_length=100, blank=True, null=True)
    confidence = models.FloatField(blank=True, null=True)


    def __str__(self):
        return f"Resume of {self.user.username} ({self.uploaded_at.strftime('%Y-%m-%d')})"