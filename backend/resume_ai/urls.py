from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('resumes/', include('resumes.urls')),
    path('analysis/', include('analysis.urls')),
    path('jobs/', include('jobs.urls')),
]
