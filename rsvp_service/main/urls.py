from django.urls import path
from . import views

urlpatterns = [
    path("rsvps/", views.rsvp_list),
    path("rsvps/create/", views.create_rsvp),
]
