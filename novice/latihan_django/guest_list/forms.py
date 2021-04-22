from django.shortcuts import render, redirect
from django import forms
from django.forms import ModelForm
from . models import Registration

class GuestForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = Registration

    # def save_data(self):
    #     form = GuestForm()
    #     if self.POST:
    #         form = GuestForm(self.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('/guest_list')
    #     return render(self, 'forms_guest_list.html',{
    #         'form' : form,
    #     })


# def add_guest(req):
#     return render(req, 'forms_guest_list.html')