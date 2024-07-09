# from django.shortcuts import render
# from .models import MonitoredSite
#
#
# def index(request):
#     sites = MonitoredSite.objects.all()
#     context = {'sites': sites}
#     return render(request, 'blog/index.html', context)

# from django.shortcuts import render, redirect
# from django.urls import reverse
# from .models import MonitoredSite
# from .forms import MonitoredSiteForm
#
#
# def home(request):
#     sites = MonitoredSite.objects.all()
#     if request.method == 'POST':
#         form = MonitoredSiteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('home'))
#     else:
#         form = MonitoredSiteForm()
#     return render(request, 'blog/index.html', {'sites': sites, 'form': form})
#
#
# def index(request):
#     if request.method == "POST":
#         form = MonitoredSiteForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = MonitoredSiteForm()
#
#     monitored_sites = MonitoredSite.objects.all()
#     return render(request, 'blog/index.html', {'form': form, 'monitored_sites': monitored_sites})

# blog/views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import MonitoredSite
from .forms import MonitoredSiteForm


def index(request):
    if request.method == "POST":
        form = MonitoredSiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))  # Przekierowanie po zapisaniu formularza
    else:
        form = MonitoredSiteForm()

    monitored_sites = MonitoredSite.objects.all()
    return render(request, 'blog/index.html', {'form': form, 'monitored_sites': monitored_sites})
