from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/submit-form/', views.submit_form, name='submit-form'),
    path('api/monitored-sites/', views.monitored_sites_list, name='monitored_sites_list'),
    path("", views.index_page, name="index_page"),  # Changed to use the new index_page view
    path("site/<int:pk>/", views.site_detail, name="site_detail"),
    path("site/<int:pk>/delete/", views.site_delete, name="site_delete"),
    path('api/check-duplicate/', views.check_duplicate, name='check_duplicate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
