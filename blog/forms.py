# from django import forms
# from .models import MonitoredSite
#
#
# class MonitoredSiteForm(forms.ModelForm):
#     class Meta:
#         model = MonitoredSite
#         fields = ['url', 'check_interval', 'search_phrase']
#         labels = {
#             'url': 'URL strony',
#             'check_interval': 'Częstotliwość sprawdzania (minuty)',
#             'search_phrase': 'Fraza do śledzenia (opcjonalne)',
#         }

# blog/forms.py

# from django import forms
# from .models import MonitoredSite
#
#
# class MonitoredSiteForm(forms.ModelForm):
#     class Meta:
#         model = MonitoredSite
#         fields = ['name', 'url', 'check_interval', 'keyword']

from django import forms
from .models import MonitoredSite


class MonitoredSiteForm(forms.ModelForm):
    class Meta:
        model = MonitoredSite
        fields = ['url', 'check_interval', 'keyword']  # Zdefiniuj tylko pola, które chcesz używać
