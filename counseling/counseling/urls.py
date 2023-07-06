from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.main_app.urls')),
    # path('acounting',include('apps.acounting.urls')),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
