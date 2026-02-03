# portfolio/urls.py
from django.contrib import admin
from django.urls import path, include  # <--- 1. Import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),    # <--- 2. Add this line
]