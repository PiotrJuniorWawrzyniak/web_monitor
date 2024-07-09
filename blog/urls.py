# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
# ]

# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('index/', views.index, name='index'),
# ]

# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Używamy views.index zamiast views.home
]
