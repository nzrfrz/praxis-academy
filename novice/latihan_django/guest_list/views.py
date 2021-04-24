from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from . models import Registration
from . forms import GuestForm, FileUpload
from . import models

# Create your views here.
def guest_list(req):
    # contoh=1+1
    guest_regist = Registration.objects.all().order_by('-created_at')
    # print(guest_regist.first().created_at)
    return render(req, 'home_guest_list.html', {
        'data' : guest_regist,
        # 'contoh':contoh
    })

def add_guest(req):
    # choices = {}
    # choices['single_choices'] = Registration.CHOICES_VALUE
    choices = Registration.CHOICES_VALUE
    choices_val = {}
    form = Registration(req.POST or None)
    choices_val['choices_input'] = form
    # multiple_choices = Registration.MULTIPLE_CHOICES_VALUE
    # print(choices)
    if req.POST:
        Registration.objects.create(
            name = req.POST['name'],
            address = req.POST['address'],
            phone_number = req.POST['phone_number'],
            choices_input = req.POST['choices_input'],
            # choices_input = form.cleaned_data.get("form"),
            # multiple_choices_input = req.POST['multiple_choices_input'],
            guest_photo = req.POST['guest_photo'],
        )
        print(choices)
        return redirect('/guest_list')
    return render(req, 'forms_guest_list.html', {
        'choices' : choices,
        # 'multiple_choices' : multiple_choices
    })
    # form = add_guest()
    # if self.POST:
    #     form = add_guest(self.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/guest_list')
    # return render(self, 'forms_guest_list.html',{
    #     'form' : form,
    # })

def update_guest(request, guest_id):
    data=models.Registration.objects.filter(pk=guest_id).first()
    if request.POST:
        Registration.objects.filter(pk=guest_id).update(
           name=request.POST['name'],
           address=request.POST['address'],
           phone_number=request.POST['phone_number'],
           guest_photo = req.POST['guest_photo']
        )
        return redirect('/guest_list')
    return render(request, 'forms_guest_list.html',{
        'data' : data,
    })
    # guest_sel = Registration.objects.get(id = guest_id)
    # guest_form = Registration(request.POST or None, instance = guest_sel)
    # if guest_form.is_valid():
    #     guest_form.save()
    #     return redirect('/guest_list')
    # return render(request, 'forms_guest_list.html',{
    #     'form' : guest_form,
    # })

def delete_guest(req, guest_id):
    data = models.Registration.objects.filter(pk=guest_id).first()
    # data = models.Registration.get(id = guest_id)
    # print(data.name)
    data.delete()
    return redirect('/guest_list')
    # if req.POST:
    #     data.delete()
    #     return redirect('/') 