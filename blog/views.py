# from django.shortcuts import render, get_object_or_404, redirect
# from .models import MonitoredSite, MonitoringResult
# from .forms import MonitoredSiteForm
# from django.http import JsonResponse
#
# # Widok do renderowania strony Reacta
# def react_app(request):
#     return render(request, 'blog/react_app.html')
#
# # Widok do obsługi formularza
# def submit_form(request):
#     if request.method == 'POST':
#         data = request.POST
#         # Przykład walidacji i odpowiedzi
#         if data.get('website_url') and data.get('frequency'):
#             # Zwracamy sukces
#             return JsonResponse({'message': 'Form submitted successfully!'}, status=200)
#         else:
#             # Zwracamy błąd
#             return JsonResponse({'error': 'Invalid form data'}, status=400)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)
#
# def index(request):
#     if request.method == "POST":
#         form = MonitoredSiteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("index")
#     else:
#         form = MonitoredSiteForm()
#
#     sites = MonitoredSite.objects.all()
#     monitoring_results = MonitoringResult.objects.order_by("-timestamp")[
#         :10
#     ]  # Pobierz ostatnie 10 wyników
#     return render(
#         request,
#         "blog/index.html",
#         {"form": form, "sites": sites, "monitoring_results": monitoring_results},
#     )
#
#
# def site_detail(request, pk):
#     site = get_object_or_404(MonitoredSite, pk=pk)
#     if request.method == "POST":
#         form = MonitoredSiteForm(request.POST, instance=site)
#         if form.is_valid():
#             form.save()
#             return redirect(
#                 "index"
#             )  # Przekierowanie do strony głównej po zapisaniu zmian
#     else:
#         form = MonitoredSiteForm(instance=site)
#
#     # Pobierz wyniki monitorowania dla konkretnej strony
#     monitoring_results = MonitoringResult.objects.filter(site=site).order_by(
#         "-timestamp"
#     )
#
#     return render(
#         request,
#         "blog/site_detail.html",
#         {"site": site, "form": form, "monitoring_results": monitoring_results},
#     )
#
#
# def site_delete(request, pk):
#     site = get_object_or_404(MonitoredSite, pk=pk)
#     if request.method == "POST":
#         site.delete()
#         return redirect("index")
#     return render(request, "blog/site_detail.html", {"site": site})

from django.shortcuts import render, get_object_or_404, redirect
from .models import MonitoredSite, MonitoringResult
from .forms import MonitoredSiteForm
from django.http import JsonResponse

# Widok do renderowania strony Reacta
def react_app(request):
    return render(request, 'blog/react_app.html')

# Widok do obsługi formularza
def submit_form(request):
    if request.method == 'POST':
        data = request.POST
        # Przykład walidacji i odpowiedzi
        if data.get('website_url') and data.get('frequency'):
            # Zwracamy sukces
            return JsonResponse({'message': 'Form submitted successfully!'}, status=200)
        else:
            # Zwracamy błąd
            return JsonResponse({'error': 'Invalid form data'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

# Nowa funkcja widoku do pobierania listy monitorowanych stron
def monitored_sites_list(request):
    if request.method == 'GET':
        sites = MonitoredSite.objects.all()
        sites_data = [
            {"id": site.id, "url": site.url, "frequency": site.frequency, "phrase": site.phrase}
            for site in sites
        ]
        return JsonResponse(sites_data, safe=False)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def index(request):
    if request.method == "POST":
        form = MonitoredSiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = MonitoredSiteForm()

    sites = MonitoredSite.objects.all()
    monitoring_results = MonitoringResult.objects.order_by("-timestamp")[
        :10
    ]  # Pobierz ostatnie 10 wyników
    return render(
        request,
        "blog/index.html",
        {"form": form, "sites": sites, "monitoring_results": monitoring_results},
    )


def site_detail(request, pk):
    site = get_object_or_404(MonitoredSite, pk=pk)
    if request.method == "POST":
        form = MonitoredSiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = MonitoredSiteForm(instance=site)

    # Pobierz wyniki monitorowania dla konkretnej strony
    monitoring_results = MonitoringResult.objects.filter(site=site).order_by(
        "-timestamp"
    )

    return render(
        request,
        "blog/site_detail.html",
        {"site": site, "form": form, "monitoring_results": monitoring_results},
    )


def site_delete(request, pk):
    site = get_object_or_404(MonitoredSite, pk=pk)
    if request.method == "POST":
        site.delete()
        return redirect("index")
    return render(request, "blog/site_detail.html", {"site": site})
