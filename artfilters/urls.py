from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home/', views.index, name = 'home'),
    path('manifesto/', views.manifesto, name = 'manifesto'),
    path('images/', views.images, name = 'images'),
    path('print/', views.print_links, name = 'print'),
    path('bio/', views.bio, name = 'bio'),
    path('contact/', views.contact, name = 'contact'),
    path('blog/', views.blog, name = 'blog'),
]
