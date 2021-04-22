from django.urls import path

from . import views
from . import forms

urlpatterns = [
    path('', views.guest_list),
    # path('add_guest/', forms.GuestForm.save_data),
    path('add_guest/', views.add_guest),
    path('update_guest/<guest_id>/', views.update_guest),
    path('delete_guest/<guest_id>/', views.delete_guest),
]