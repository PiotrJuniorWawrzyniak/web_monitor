from django.shortcuts import render, redirect
from django.urls import reverse
from .models import MonitoredSite
from .forms import MonitoredSiteForm


def index(request):
    if request.method == "POST":
        form = MonitoredSiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
    else:
        form = MonitoredSiteForm()

    monitored_sites = MonitoredSite.objects.all()
    return render(request, 'blog/index.html', {'form': form, 'monitored_sites': monitored_sites})
