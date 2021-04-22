from django.urls import path

from . import views
from . import forms
# from . import forms

urlpatterns = [
    path('', views.daftar_hadir_home),
    path('add_guest', forms.form_input)
]