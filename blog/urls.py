# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('api/submit-form/', views.submit_form, name='submit-form'),
#     path('react/', views.react_app, name='react_app'),
#     path("", views.index, name="index"),
#     path("site/<int:pk>/", views.site_detail, name="site_detail"),
#     path("site/<int:pk>/delete/", views.site_delete, name="site_delete"),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('api/submit-form/', views.submit_form, name='submit-form'),
    path('api/monitored-sites/', views.monitored_sites_list, name='monitored_sites_list'),
    path('react/', views.react_app, name='react_app'),
    path("", views.index, name="index"),
    path("site/<int:pk>/", views.site_detail, name="site_detail"),
    path("site/<int:pk>/delete/", views.site_delete, name="site_delete"),
]
