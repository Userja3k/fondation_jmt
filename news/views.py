from django.shortcuts import render
from .models import Event
from django.utils import timezone

def news_list(request):
    """View for displaying upcoming events."""
    today = timezone.now().date()
    upcoming_events = Event.objects.filter(date__gte=today).order_by('date')
    
    context = {
        'upcoming_events': upcoming_events,
    }
    
    return render(request, 'news/news_list.html', context)

def event_detail(request, event_id):
    """View for displaying event details."""
    event = get_object_or_404(Event, id=event_id)
    
    context = {
        'event': event,
    }
    
    return render(request, 'news/event_detail.html', context)