from celery import shared_task
import requests
from .models import MonitoredSite, MonitoringResult


@shared_task
def check_sites(site_id):
    try:
        site = MonitoredSite.objects.get(id=site_id)
        response = requests.get(site.url)
        response.raise_for_status()

        result = "Strona się nie zmieniła"
        if response.text != site.last_content:
            result = "Strona się zmieniła"
            site.last_content = response.text
            site.save()

        if site.keyword in response.text and (site.last_phrase_status is None or not site.last_phrase_status):
            result = "Fraza została znaleziona"
            site.last_phrase_status = True
            site.save()
        elif site.keyword not in response.text and (site.last_phrase_status is None or site.last_phrase_status):
            result = "Fraza została usunięta"
            site.last_phrase_status = False
            site.save()

        MonitoringResult.objects.create(site=site, result=result)

    except requests.RequestException as e:
        print(f"Error checking site {site.url}: {e}")
    except MonitoredSite.DoesNotExist:
        print(f"Site with id {site_id} does not exist")
