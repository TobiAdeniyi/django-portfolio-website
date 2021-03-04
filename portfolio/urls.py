from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from jobs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('jobs/<int:job_id>', views.detail, name='detail'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
