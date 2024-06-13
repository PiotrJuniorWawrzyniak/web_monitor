from django.shortcuts import render
from .models import MonitoredSite


def index(request):
    sites = MonitoredSite.objects.all()
    context = {'sites': sites}
    return render(request, 'blog/index.html', context)
