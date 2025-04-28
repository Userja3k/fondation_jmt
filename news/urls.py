from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
]