from django.shortcuts import render, redirect

def form_input(req):
    return render(req, 'daftarhadir/form_input.html')

