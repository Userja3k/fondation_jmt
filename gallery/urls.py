from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery_list, name='gallery_list'),
    path('item/<int:item_id>/', views.gallery_item_detail, name='gallery_item_detail'),
    path('collection/<int:collection_id>/', views.gallery_collection_detail, name='gallery_collection_detail'),
]