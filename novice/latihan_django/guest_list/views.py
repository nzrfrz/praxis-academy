from django.shortcuts import get_object_or_404, render, redirect
from django.core.files.storage import FileSystemStorage

from . models import Registration
from . import models

# Create your views here.
def guest_list(req):
    # contoh=1+1
    guest_regist = Registration.objects.all().order_by('-created_at')
    objects_checkbox = Registration.objects.values_list('multiple_choices_input')
    x = {}
    x['a'] = objects_checkbox
    # print(Registration.objects.exclude(multiple_choices_input='[]'))
    for i in objects_checkbox:
        for j in i:
            checkbox_values = j[1:-1]
    # print(', '.join(str(i) for i in objects_all))
    return render(req, 'home_guest_list.html', {
        'data' : guest_regist,
        'checkbox_values' : guest_regist,
        # 'contoh':contoh
    })

# def checkbox_values(self):
#     checkbox_list = Registration.objects.values_list('multiple_choices_input')
#     for i in objects_checkbox:
#         for j in i:
#             checkbox_list = j[1:-1]
#     return checkbox_list

def add_guest(req):
    choices = Registration.CHOICES_VALUE
    multiple_choices = Registration.MULTIPLE_CHOICES_VALUE
    # i = []
    # i.append(multiple_choices)
    # print(i)
    if req.POST:
        Registration.objects.create(
            name = req.POST['name'],
            address = req.POST['address'],
            phone_number = req.POST['phone_number'],
            choices_input = req.POST['choices_input'],
            multiple_choices_input = req.POST.getlist('multiple_choices_input'),
            # multiple_choices_input = req.POST.get('multiple_choices_input'),
            guest_photo = req.FILES['guest_photo'],
        )
        return redirect('/guest_list')
    return render(req, 'forms_guest_list.html', {
        'choices' : choices,
        'multiple_choices' : multiple_choices
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
    choices = Registration.CHOICES_VALUE
    multiple_choices = Registration.MULTIPLE_CHOICES_VALUE
    if request.POST:
        Registration.objects.filter(pk=guest_id).update(
           name=request.POST['name'],
           address=request.POST['address'],
           phone_number=request.POST['phone_number'],
           choices_input = request.POST['choices_input'],
           multiple_choices_input = request.POST.getlist('multiple_choices_input'),
           guest_photo = request.FILES['guest_photo']
        )
        return redirect('/guest_list')
    return render(request, 'forms_guest_list.html',{
        'data' : data,
        'choices' : choices,
        'multiple_choices' : multiple_choices
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