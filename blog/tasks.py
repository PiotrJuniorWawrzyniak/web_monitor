from celery import shared_task
import requests
from .models import MonitoredSite


@shared_task
def check_site(site_id=None):
    if site_id:
        sites = MonitoredSite.objects.filter(id=site_id)
    else:
        sites = MonitoredSite.objects.all()

    for site in sites:
        try:
            response = requests.get(site.url)
            response.raise_for_status()  # sprawdzenie, czy odpowiedź jest poprawna

            if response.text != site.last_content:
                # Strona się zmieniła
                site.last_content = response.text
                site.save()
                # Wysyłanie powiadomienia o zmianie (np. email)

            if site.phrase in response.text and (site.last_phrase_status is None or not site.last_phrase_status):
                # Fraza została znaleziona
                site.last_phrase_status = True
                site.save()
                # Wysyłanie powiadomienia o znalezieniu frazy (np. email)
            elif site.phrase not in response.text and (site.last_phrase_status is None or site.last_phrase_status):
                # Fraza została usunięta
                site.last_phrase_status = False
                site.save()
                # Wysyłanie powiadomienia o usunięciu frazy (np. email)

        except requests.RequestException as e:
            # Logowanie błędu (np. do pliku logów)
            print(f"Error checking site {site.url}: {e}")
