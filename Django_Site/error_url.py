from django.urls import path
from django.urls import re_path
from django.views.generic import RedirectView
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.error_page, name='error_page'),
    re_path(r'^', RedirectView.as_view(url='error_page'))
]