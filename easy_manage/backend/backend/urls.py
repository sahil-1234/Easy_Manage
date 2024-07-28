"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todo import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'tasks', views.TodoView, 'task')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
    
]
