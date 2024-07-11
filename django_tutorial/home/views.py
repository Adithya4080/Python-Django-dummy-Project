from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments
# Create your views here.
def index(request):

    # person = {
    #     'name': 'John',
    #     'age': '30',
    #     'Place' : 'Calicut'
    # }

    # numbers = {
    #     'num1': 0,
    # }
    # number = {
    #     'num1': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    # }
    return render(request, 'index.html' )

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')

def doctors(request):
    return render(request, 'doctors.html')

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)