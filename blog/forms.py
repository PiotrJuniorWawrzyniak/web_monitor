from django import forms
from .models import MonitoredSite


class MonitoredSiteForm(forms.ModelForm):
    class Meta:
        model = MonitoredSite
        fields = ["url", "check_interval", "keyword"]
        labels = {
            "url": "Adres strony",
            "check_interval": "Częstotliwość monitorowania",
            "keyword": "Wyszukiwana fraza",
        }

    def clean_url(self):
        url = self.cleaned_data.get("url")
        if MonitoredSite.objects.filter(url=url).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Ta strona jest już monitorowana.")
        return url

    def __init__(self, *args, **kwargs):
        super(MonitoredSiteForm, self).__init__(*args, **kwargs)
        self.fields["check_interval"].widget.attrs.update({"min": "1"})
