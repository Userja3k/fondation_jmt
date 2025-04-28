from django.shortcuts import render, get_object_or_404
from .models import ArchivedService, Debate
from django.db.models import Q

def archive_list(request):
    """View for displaying archived services and debates."""
    # Get search parameters
    search_query = request.GET.get('q', '')
    date_query = request.GET.get('date', '')
    
    # Filter services based on search parameters
    services = ArchivedService.objects.all()
    debates = Debate.objects.all()
    
    if search_query:
        services = services.filter(
            Q(title__icontains=search_query) | 
            Q(theme__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
        debates = debates.filter(
            Q(title__icontains=search_query) | 
            Q(topic__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    if date_query:
        services = services.filter(date=date_query)
        debates = debates.filter(date=date_query)
    
    context = {
        'services': services,
        'debates': debates,
        'search_query': search_query,
        'date_query': date_query,
    }
    
    return render(request, 'archive/archive_list.html', context)

def service_detail(request, service_id):
    """View for displaying service details."""
    service = get_object_or_404(ArchivedService, id=service_id)
    
    context = {
        'service': service,
    }
    
    return render(request, 'archive/service_detail.html', context)

def debate_detail(request, debate_id):
    """View for displaying debate details."""
    debate = get_object_or_404(Debate, id=debate_id)
    
    context = {
        'debate': debate,
    }
    
    return render(request, 'archive/debate_detail.html', context)