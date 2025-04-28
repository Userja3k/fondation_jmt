from django.urls import path
from . import views

app_name = 'theology'

urlpatterns = [
    path('', views.theology_list, name='theology_list'),
    path('course/<int:course_id>/', views.theology_detail, name='theology_detail'),
]