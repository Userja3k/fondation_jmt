from django.shortcuts import render
from .models import AboutContent, Founder, Partner

def about(request):
    """View for about page."""
    content = AboutContent.objects.first()  # Get the first content object
    founders = Founder.objects.all()
    partners = Partner.objects.all()
    
    context = {
        'content': content,
        'founders': founders,
        'partners': partners,
    }
    
    return render(request, 'about/about.html', context)