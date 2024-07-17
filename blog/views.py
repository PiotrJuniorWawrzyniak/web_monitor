from django.shortcuts import render, redirect, get_object_or_404
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
    results = {site.pk: MonitoringResult.objects.filter(site=site).order_by('-timestamp').first() for site in sites}
    return render(request, 'blog/index.html', {'form': form, 'sites': sites, 'results': results})


def site_detail(request, pk):
    site = get_object_or_404(MonitoredSite, pk=pk)
    if request.method == 'POST':
        form = MonitoredSiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MonitoredSiteForm(instance=site)

    return render(request, 'blog/site_detail.html', {'form': form, 'site': site})


def site_delete(request, pk):
    site = get_object_or_404(MonitoredSite, pk=pk)
    if request.method == 'POST':
        site.delete()
        return redirect('index')
    return render(request, 'blog/site_confirm_delete.html', {'site': site})
