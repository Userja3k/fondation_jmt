from django.shortcuts import render
from django.db.models import Prefetch
from .models import WeeklyService, HomePageSection, SpecialEvent, Culte
from news.models import Event
from archive.models import ArchivedService
from theology.models import TheologyCourse
from django.shortcuts import redirect

def home(request):
    from django.utils import timezone
    from datetime import timedelta

    weekly_service = WeeklyService.objects.order_by('-date').first()
    
    culte_semaine = SpecialEvent.objects.filter(est_culte_de_la_semaine=True).first()
    if culte_semaine and not culte_semaine.is_active():
        culte_semaine = None
    
    cutoff_datetime = timezone.now() - timedelta(days=7)
    special_events = SpecialEvent.objects.filter(created_at__gte=cutoff_datetime).exclude(est_culte_de_la_semaine=True)
    
    sections = HomePageSection.objects.filter(is_active=True).order_by('display_order')
    
    section_content = {}
    for section in sections:
        if section.section_type == 'cultes':
            section_content[section.id] = Culte.objects.order_by('-date')[:3]
        elif section.section_type == 'evenements':
            # Removed is_upcoming filter temporarily
            section_content[section.id] = Event.objects.order_by('date')[:3]
        elif section.section_type == 'theologie':
            section_content[section.id] = TheologyCourse.objects.order_by('-date')[:3]
    
    context = {
        'weekly_service': weekly_service,
        'culte_semaine': culte_semaine,
        'special_events': special_events,
        'sections': sections,
        'section_content': section_content,
    }
    
    return render(request, 'home/home.html', context)


def toggle_theme(request):
    """Toggle between light and dark theme."""
    current_theme = request.COOKIES.get('jmt_theme', 'light')
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    
    # Set theme cookie
    new_theme = 'dark' if current_theme == 'light' else 'light'
    response.set_cookie('jmt_theme', new_theme, max_age=31536000)  # 1 year
    
    return response
