from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('news/', include('news.urls')),
    path('archive/', include('archive.urls')),
    path('gallery/', include('gallery.urls')),
    path('theology/', include('theology.urls')),
    path('about/', include('about.urls')),
    path('users/', include('users.urls')),
    path('custom-admin/', include('custom_admin.urls', namespace='custom_admin')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)