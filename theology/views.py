from django.shortcuts import render, get_object_or_404
from .models import TheologyCourse

def theology_list(request):
    """View for displaying theology courses."""
    # Filter courses by type
    online_courses = TheologyCourse.objects.filter(course_type='online')
    inperson_courses = TheologyCourse.objects.filter(course_type='inperson')
    conferences = TheologyCourse.objects.filter(course_type='conference')
    seminars = TheologyCourse.objects.filter(course_type='seminar')
    
    context = {
        'online_courses': online_courses,
        'inperson_courses': inperson_courses,
        'conferences': conferences,
        'seminars': seminars,
    }
    
    return render(request, 'theology/theology_list.html', context)

def theology_detail(request, course_id):
    """View for displaying theology course details."""
    course = get_object_or_404(TheologyCourse, id=course_id)
    
    context = {
        'course': course,
    }
    
    return render(request, 'theology/theology_detail.html', context)