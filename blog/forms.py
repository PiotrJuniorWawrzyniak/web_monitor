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

    def clean_url(self):
        url = self.cleaned_data.get('url')
        if MonitoredSite.objects.filter(url=url).exists():
            raise forms.ValidationError("Ta strona jest już monitorowana.")
        return url
