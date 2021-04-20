from django.shortcuts import render, redirect

# Create your views here.
def daftar_hadir_home(req):
    return render(req, 'daftarhadir/index_daftar_hadir.html')

# def input_guest(req):
#     return render(req, 'form_input.html')
