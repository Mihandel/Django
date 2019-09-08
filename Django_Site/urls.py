from django.urls import path
from django.urls import re_path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('error_page', views.error_page, name='error_page'),
    path('crosswords', RedirectView.as_view(url='crosswords/', permanent=True)),
    re_path(r'crosswords/$', views.CrosswordView.as_view(), name='crosswords'),
    path('crosswords/<int:pk>', views.CrosswordDetailedView.as_view(), name='crosswords'),
    path('crosswords/error_page', views.error_page, name='error_page'),
    re_path(r'^', RedirectView.as_view(url='error_page'))
]