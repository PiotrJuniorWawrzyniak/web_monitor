# from django.shortcuts import render, get_object_or_404, redirect
# from .models import MonitoredSite, MonitoringResult
# from .forms import MonitoredSiteForm
# from django.http import JsonResponse
# from django.db import IntegrityError
# from django.core.validators import URLValidator
# from django.core.exceptions import ValidationError
# import json
#
#
# def index_page(request):
#     return render(request, 'frontend/build/index.html')  # Render the React app
#
#
# def submit_form(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         print(f"Otrzymane dane z frontendu: {data}")  # Logowanie pełnych danych
#
#         url = data.get('url')
#         frequency = data.get('frequency')
#         keyword = data.get('keyword')
#         print(f"URL: {url}, Frequency: {frequency}, Keyword: {keyword}")  # Logowanie kluczowych danych
#
#         if url and frequency and keyword:
#             url_validator = URLValidator()
#             try:
#                 # Walidacja URL przed próbą zapisania
#                 url_validator(url)
#                 MonitoredSite.objects.create(
#                     url=url,
#                     keyword=keyword,
#                     check_interval=frequency
#                 )
#                 print("Dane zostały poprawnie zapisane w bazie")
#                 return JsonResponse({'message': 'Form submitted and site added successfully!'}, status=200)
#             except ValidationError:
#                 print("Walidacja URL nie przeszła")
#                 return JsonResponse({'error': 'Invalid URL'}, status=400)
#             except IntegrityError:
#                 print("Strona o podanym URL już istnieje")
#                 return JsonResponse({'error': 'This URL is already being monitored'}, status=400)
#         else:
#             print("Niekompletne dane: brakujące pola")
#             return JsonResponse({'error': 'Invalid form data'}, status=400)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)
#
#
# # Widok do pobierania listy monitorowanych stron
# def monitored_sites_list(request):
#     if request.method == 'GET':
#         sites = MonitoredSite.objects.all()
#         sites_data = [
#             {
#                 "id": site.id,
#                 "url": site.url,
#                 "check_interval": site.check_interval,
#                 "keyword": site.keyword,
#                 "last_phrase_status": site.last_phrase_status  # Dodaj status
#             }
#             for site in sites
#         ]
#         return JsonResponse(sites_data, safe=False)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)
#
#
# # Widok szczegółów strony
# def site_detail(request, pk):
#     site = get_object_or_404(MonitoredSite, pk=pk)
#     if request.method == "POST":
#         form = MonitoredSiteForm(request.POST, instance=site)
#         if form.is_valid():
#             form.save()
#             return redirect("index_page")  # Redirect to the new index_page
#     else:
#         form = MonitoredSiteForm(instance=site)
#
#     monitoring_results = MonitoringResult.objects.filter(site=site).order_by("-timestamp")
#
#     return render(
#         request,
#         "blog/site_detail.html",
#         {"site": site, "form": form, "monitoring_results": monitoring_results},
#     )
#
#
# # Usuwanie monitorowanej strony
# def site_delete(request, pk):
#     site = get_object_or_404(MonitoredSite, pk=pk)
#     if request.method == "POST":
#         site.delete()
#         return redirect("index_page")  # Redirect to the new index_page
#     return render(request, "blog/site_detail.html", {"site": site})
#
#
# # Sprawdzenie duplikatu URL
# def check_duplicate(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         url = data.get('url')
#
#         if url:
#             exists = MonitoredSite.objects.filter(url=url).exists()
#             if exists:
#                 return JsonResponse({'duplicate': True}, status=200)
#             return JsonResponse({'duplicate': False}, status=200)
#         return JsonResponse({'error': 'Invalid data'}, status=400)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)

from django.shortcuts import render, get_object_or_404, redirect
from .models import MonitoredSite, MonitoringResult
from .forms import MonitoredSiteForm
from django.http import JsonResponse
from django.db import IntegrityError
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import json


def index_page(request):
    return render(request, 'frontend/build/index.html')  # Render the React app


def submit_form(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(f"Otrzymane dane z frontendu: {data}")  # Logowanie pełnych danych

        url = data.get('url')
        check_interval = data.get('check_interval')
        keyword = data.get('keyword')
        print(f"URL: {url}, Check Interval: {check_interval}, Keyword: {keyword}")  # Logowanie kluczowych danych

        if url and check_interval and keyword:
            url_validator = URLValidator()
            try:
                # Walidacja URL przed próbą zapisania
                url_validator(url)
                MonitoredSite.objects.create(
                    url=url,
                    keyword=keyword,
                    check_interval=check_interval
                )
                print("Dane zostały poprawnie zapisane w bazie")
                return JsonResponse({'message': 'Form submitted and site added successfully!'}, status=200)
            except ValidationError:
                print("Walidacja URL nie przeszła")
                return JsonResponse({'error': 'Invalid URL'}, status=400)
            except IntegrityError:
                print("Strona o podanym URL już istnieje")
                return JsonResponse({'error': 'This URL is already being monitored'}, status=400)
        else:
            print("Niekompletne dane: brakujące pola")
            return JsonResponse({'error': 'Invalid form data'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


# Widok do pobierania listy monitorowanych stron
def monitored_sites_list(request):
    if request.method == 'GET':
        sites = MonitoredSite.objects.all()
        sites_data = [
            {
                "id": site.id,
                "url": site.url,
                "check_interval": site.check_interval,
                "keyword": site.keyword,
                "last_phrase_status": site.last_phrase_status  # Dodaj status
            }
            for site in sites
        ]
        return JsonResponse(sites_data, safe=False)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


# Widok szczegółów strony
def site_detail(request, pk):
    site = get_object_or_404(MonitoredSite, pk=pk)
    if request.method == "POST":
        form = MonitoredSiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect("index_page")  # Redirect to the new index_page
    else:
        form = MonitoredSiteForm(instance=site)

    monitoring_results = MonitoringResult.objects.filter(site=site).order_by("-timestamp")

    return render(
        request,
        "blog/site_detail.html",
        {"site": site, "form": form, "monitoring_results": monitoring_results},
    )


# Usuwanie monitorowanej strony
def site_delete(request, pk):
    site = get_object_or_404(MonitoredSite, pk=pk)
    if request.method == "POST":
        site.delete()
        return redirect("index_page")  # Redirect to the new index_page
    return render(request, "blog/site_detail.html", {"site": site})


# Sprawdzenie duplikatu URL
def check_duplicate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        url = data.get('url')

        if url:
            exists = MonitoredSite.objects.filter(url=url).exists()
            if exists:
                return JsonResponse({'duplicate': True}, status=200)
            return JsonResponse({'duplicate': False}, status=200)
        return JsonResponse({'error': 'Invalid data'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
