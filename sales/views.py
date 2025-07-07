# sales/views.py

from django.shortcuts import render

def sales_home(request):
    return render(request, 'sales/home.html')