from django.contrib import admin
from .models import Prediction, SkillSuggestion

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('resume', 'predicted_role', 'confidence', 'created_at')
    search_fields = ('predicted_role', 'resume__user__username')

@admin.register(SkillSuggestion)
class SkillSuggestionAdmin(admin.ModelAdmin):
    list_display = ('resume', 'missing_skill', 'suggested_for_role')
    search_fields = ('missing_skill', 'suggested_for_role', 'resume__user__username')
