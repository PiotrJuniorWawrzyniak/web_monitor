import requests
from bs4 import BeautifulSoup
from celery import shared_task
from .models import MonitoredSite, MonitoringResult


@shared_task
def check_sites(site_id):
    try:
        site = MonitoredSite.objects.get(id=site_id)
    except MonitoredSite.DoesNotExist:
        return

    response = requests.get(site.url)
    content = response.text

    # Sprawdź, czy zawartość strony się zmieniła
    if site.last_content != content:
        site.last_content = content
        site.save()

        # Dodaj wpis w MonitoringResult
        MonitoringResult.objects.create(site=site, result='Treść zmieniona')

    # Sprawdź, czy fraza jest obecna w zawartości strony
    soup = BeautifulSoup(content, 'html.parser')
    phrase_status = site.keyword in soup.text

    # Jeśli status frazy się zmienił, zaktualizuj go
    if site.last_phrase_status != phrase_status:
        site.last_phrase_status = phrase_status
        site.save()

        if phrase_status:
            result = f"Fraza '{site.keyword}' została znaleziona."
        else:
            result = f"Fraza '{site.keyword}' nie została znaleziona."

        # Dodaj wpis w MonitoringResult
        MonitoringResult.objects.create(site=site, result=result)
