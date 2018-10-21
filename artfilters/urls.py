""" The art site urls """
from django.urls import path

from . import views

app_name = 'artfilters'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home/', views.IndexView.as_view(), name='home'),
    path('manifesto/', views.ManifestoView.as_view(), name='manifesto'),
    path('images/', views.ImagesView.as_view(), name='images'),
    path('print/', views.PrintView.as_view(), name='print'),
    path('bio/', views.BioView.as_view(), name='bio'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('blog/', views.BlogView.as_view(), name='blog'),
]
