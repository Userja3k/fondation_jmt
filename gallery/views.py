from django.shortcuts import render, get_object_or_404
from .models import GalleryItem, GalleryCollection

def gallery_list(request):
    """View for displaying gallery items."""
    items = GalleryItem.objects.all()
    collections = GalleryCollection.objects.all()
    
    context = {
        'items': items,
        'collections': collections,
    }
    
    return render(request, 'gallery/gallery_list.html', context)

def gallery_item_detail(request, item_id):
    """View for displaying gallery item details."""
    item = get_object_or_404(GalleryItem, id=item_id)
    
    context = {
        'item': item,
    }
    
    return render(request, 'gallery/gallery_item_detail.html', context)

def gallery_collection_detail(request, collection_id):
    """View for displaying gallery collection details."""
    collection = get_object_or_404(GalleryCollection, id=collection_id)
    
    context = {
        'collection': collection,
    }
    
    return render(request, 'gallery/gallery_collection_detail.html', context)