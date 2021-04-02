from django.urls.resolvers import URLPattern
from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contacts',views.contact,name='contacts'),
]