from django.urls import path
from . import views

app_name = 'archive'

urlpatterns = [
    path('', views.archive_list, name='archive_list'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('debate/<int:debate_id>/', views.debate_detail, name='debate_detail'),
]