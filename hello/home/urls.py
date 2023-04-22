from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Maan Ice-cream"
admin.site.site_title = "Maan Ice-creams"
admin.site.index_title = "Welcome to Maan Ice-cream"

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='Contact'),
]
