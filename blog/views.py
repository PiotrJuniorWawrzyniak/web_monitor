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
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        url = data.get('url')
        check_interval = int(data.get('check_interval'))
        keyword = data.get('keyword')

        if not url or not check_interval or not keyword:
            return JsonResponse({'error': 'Incomplete form data'}, status=400)

        url_validator = URLValidator()
        try:
            url_validator(url)  # Walidacja URL
            site, created = MonitoredSite.objects.get_or_create(
                url=url,
                defaults={'keyword': keyword, 'check_interval': check_interval}
            )

            if not created:
                return JsonResponse({'error': 'This URL is already being monitored'}, status=400)

            return JsonResponse({'message': 'Form submitted and site added successfully!'}, status=200)

        except ValidationError:
            return JsonResponse({'error': 'Invalid URL'}, status=400)
        except IntegrityError:
            return JsonResponse({'error': 'This URL is already being monitored'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def monitored_sites_list(request):
    if request.method == 'GET':
        sites = MonitoredSite.objects.all()
        sites_data = [
            {
                "id": site.id,
                "url": site.url,
                "check_interval": site.check_interval,
                "keyword": site.keyword,
                "last_phrase_status": site.last_phrase_status
            }
            for site in sites
        ]
        return JsonResponse(sites_data, safe=False)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


def site_detail(request, pk):
    site = get_object_or_404(MonitoredSite, pk=pk)
    if request.method == "POST":
        form = MonitoredSiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect("index_page")
    else:
        form = MonitoredSiteForm(instance=site)

    monitoring_results = MonitoringResult.objects.filter(site=site).order_by("-timestamp")

    return render(
        request,
        "blog/site_detail.html",
        {"site": site, "form": form, "monitoring_results": monitoring_results},
    )


def site_delete(request, pk):
    site = get_object_or_404(MonitoredSite, pk=pk)
    if request.method == "POST":
        site.delete()
        return redirect("index_page")
    return render(request, "blog/site_detail.html", {"site": site})


def check_duplicate(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        url = data.get('url')

        if not url:
            return JsonResponse({'error': 'Invalid data'}, status=400)

        exists = MonitoredSite.objects.filter(url=url).exists()
        return JsonResponse({'duplicate': exists}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
