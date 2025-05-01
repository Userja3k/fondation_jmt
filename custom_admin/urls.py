from django.urls import path
from .views import dashboard, home_manager, news_selector, archive_editor, gallery_manager, theology_manager

app_name = 'custom_admin'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('home/', home_manager, name='home_manager'),
    path('news/', news_selector, name='news_selector'),
    path('archive/', archive_editor, name='archive_editor'),
    path('gallery/', gallery_manager, name='gallery_manager'),
    path('theology/', theology_manager, name='theology_manager'),
]
