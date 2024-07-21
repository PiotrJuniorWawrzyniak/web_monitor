from django.shortcuts import render, get_object_or_404, redirect
from .models import MonitoredSite, MonitoringResult
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
    monitoring_results = MonitoringResult.objects.order_by('-timestamp')[:10]  # Pobierz ostatnie 10 wyników
    return render(request, 'blog/index.html', {'form': form, 'sites': sites, 'monitoring_results': monitoring_results})


def site_detail(request, pk):
    site = get_object_or_404(MonitoredSite, pk=pk)
    if request.method == 'POST':
        form = MonitoredSiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MonitoredSiteForm(instance=site)
    return render(request, 'blog/site_detail.html', {'site': site, 'form': form})


def site_delete(request, pk):
    site = get_object_or_404(MonitoredSite, pk=pk)
    if request.method == 'POST':
        site.delete()
        return redirect('index')
    return render(request, 'blog/site_detail.html', {'site': site})
