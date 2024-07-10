from django.shortcuts import render, redirect
from .models import MonitoredSite
from .forms import MonitoredSiteForm


def index(request):
    if request.method == 'POST':
        form = MonitoredSiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MonitoredSiteForm()

    sites = MonitoredSite.objects.all()
    return render(request, 'blog/index.html', {'form': form, 'sites': sites})
