from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('main.urls')),
    path('auth/', include('users.urls')),
    path('stats/', include('stats.urls')),
]