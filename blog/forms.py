from django import forms
from .models import MonitoredSite


class MonitoredSiteForm(forms.ModelForm):
    class Meta:
        model = MonitoredSite
        fields = ['url', 'check_interval', 'keyword']
        labels = {
            'url': 'Adres strony',
            'check_interval': 'Częstotliwość monitorowania',
            'keyword': 'Wyszukiwana fraza',
        }
