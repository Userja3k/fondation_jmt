from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from home.models import SpecialEvent, Culte
from theology.models import TheologyCourse
from news.models import Event
from archive.models import ArchivedService
from gallery.models import GalleryItem, GalleryCollection, GalleryCollectionItem
from django.forms import modelform_factory

@staff_member_required
def dashboard(request):
    sections = [
        {'name': 'Home Manager', 'url': '/custom-admin/home/'},
        {'name': 'News Selector', 'url': '/custom-admin/news/'},
        {'name': 'Archive Editor', 'url': '/custom-admin/archive/'},
        {'name': 'Gallery Manager', 'url': '/custom-admin/gallery/'},
        {'name': 'Théologie Manager', 'url': '/custom-admin/theology/'},
    ]
    return render(request, 'custom_admin/dashboard.html', {'sections': sections})

@staff_member_required
def home_manager(request):
    SpecialEventForm = modelform_factory(SpecialEvent, fields='__all__')
    CulteForm = modelform_factory(Culte, fields='__all__')
    TheologyCourseForm = modelform_factory(TheologyCourse, fields='__all__')

    special_events = SpecialEvent.objects.all().order_by('-created_at')
    cultes = Culte.objects.all().order_by('-date')
    theology_courses = TheologyCourse.objects.all().order_by('-date')

    special_event_form = None
    culte_form = None
    theology_course_form = None

    if request.method == 'POST':
        if 'add_special_event' in request.POST:
            special_event_form = SpecialEventForm(request.POST)
            if special_event_form.is_valid():
                special_event_form.save()
                return redirect('custom_admin:home_manager')
        elif 'add_culte' in request.POST:
            culte_form = CulteForm(request.POST, request.FILES)
            if culte_form.is_valid():
                culte_form.save()
                return redirect('custom_admin:home_manager')
        elif 'add_theology_course' in request.POST:
            theology_course_form = TheologyCourseForm(request.POST, request.FILES)
            if theology_course_form.is_valid():
                theology_course_form.save()
                return redirect('custom_admin:home_manager')
    else:
        special_event_form = SpecialEventForm()
        culte_form = CulteForm()
        theology_course_form = TheologyCourseForm()

    # If any form is still None (e.g., POST with invalid form), initialize it empty to avoid UnboundLocalError
    if special_event_form is None:
        special_event_form = SpecialEventForm()
    if culte_form is None:
        culte_form = CulteForm()
    if theology_course_form is None:
        theology_course_form = TheologyCourseForm()

    context = {
        'special_events': special_events,
        'cultes': cultes,
        'theology_courses': theology_courses,
        'special_event_form': special_event_form,
        'culte_form': culte_form,
        'theology_course_form': theology_course_form,
    }
    return render(request, 'custom_admin/home_manager.html', context)

@staff_member_required
def news_selector(request):
    events = Event.objects.all().order_by('-date')

    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_events')
        # Reset all events to not upcoming
        Event.objects.update(is_upcoming=False)
        # Set selected events to upcoming
        Event.objects.filter(id__in=selected_ids).update(is_upcoming=True)
        return redirect('custom_admin:news_selector')

    context = {
        'events': events,
    }
    return render(request, 'custom_admin/news_selector.html', context)

@staff_member_required
def archive_editor(request):
    archived_services = ArchivedService.objects.all().order_by('-date')

    if request.method == 'POST':
        # Example: handle archiving or editing logic here
        pass

    context = {
        'archived_services': archived_services,
    }
    return render(request, 'custom_admin/archive_editor.html', context)

@staff_member_required
def gallery_manager(request):
    GalleryCollectionForm = modelform_factory(GalleryCollection, fields='__all__')
    GalleryItemForm = modelform_factory(GalleryItem, fields='__all__')
    GalleryCollectionItemForm = modelform_factory(GalleryCollectionItem, fields='__all__')

    collections = GalleryCollection.objects.all().order_by('-date')
    items = GalleryItem.objects.all().order_by('-date')
    collection_items = GalleryCollectionItem.objects.all().order_by('-id')

    collection_form = None
    item_form = None
    collection_item_form = None

    if request.method == 'POST':
        if 'add_collection' in request.POST:
            collection_form = GalleryCollectionForm(request.POST)
            if collection_form.is_valid():
                collection_form.save()
                return redirect('custom_admin:gallery_manager')
        elif 'add_item' in request.POST:
            item_form = GalleryItemForm(request.POST, request.FILES)
            if item_form.is_valid():
                item_form.save()
                return redirect('custom_admin:gallery_manager')
        elif 'add_collection_item' in request.POST:
            collection_item_form = GalleryCollectionItemForm(request.POST, request.FILES)
            if collection_item_form.is_valid():
                collection_item_form.save()
                return redirect('custom_admin:gallery_manager')
    else:
        collection_form = GalleryCollectionForm()
        item_form = GalleryItemForm()
        collection_item_form = GalleryCollectionItemForm()

    # Initialize forms if still None (e.g., POST with invalid form) to avoid UnboundLocalError
    if collection_form is None:
        collection_form = GalleryCollectionForm()
    if item_form is None:
        item_form = GalleryItemForm()
    if collection_item_form is None:
        collection_item_form = GalleryCollectionItemForm()

    context = {
        'collections': collections,
        'items': items,
        'collection_items': collection_items,
        'collection_form': collection_form,
        'item_form': item_form,
        'collection_item_form': collection_item_form,
    }
    return render(request, 'custom_admin/gallery_manager.html', context)

@staff_member_required
def theology_manager(request):
    TheologyCourseForm = modelform_factory(TheologyCourse, fields='__all__')

    theology_courses = TheologyCourse.objects.all().order_by('-date')

    if request.method == 'POST':
        form = TheologyCourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('custom_admin:theology_manager')
    else:
        form = TheologyCourseForm()

    context = {
        'theology_courses': theology_courses,
        'form': form,
    }
    return render(request, 'custom_admin/theology_manager.html', context)
