from django.shortcuts import render
from .models import Gallery,  Event

def home(request):
    gallery_items = Gallery.objects.all()
    events =  Event.objects.all()
    # 2. Add it to the context dictionary
    context = {
        'gallery': gallery_items,
        'events':events,
    }
    return render(request,"index.html", context=context)

# Create your views here.
