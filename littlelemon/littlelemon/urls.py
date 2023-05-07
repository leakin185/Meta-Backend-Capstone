from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from restaurant import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant', include('restaurant.urls')),
]
