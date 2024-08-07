from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("site/<int:pk>/", views.site_detail, name="site_detail"),
    path("site/<int:pk>/delete/", views.site_delete, name="site_delete"),
]
