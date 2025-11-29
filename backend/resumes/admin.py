from django.contrib import admin
from .models import Resume
# Register your models here.

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user','uploaded_at','predicted_role', 'confidence')
    search_fields = ('user__username', 'predicted_role')