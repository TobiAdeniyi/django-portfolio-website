from django.contrib import admin
from django.urls import path
from jobs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home')
]
