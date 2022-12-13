from django.shortcuts import render
from django.views.generic import View  #importamos la vista
from django.http import HttpResponse

# Create your views here.

class HelloWorld(View):
    def get(self, request):
        data = {
            'name': 'Estefania Noelia Turin',
            'years': 22,
            'codes': ['Python','Django','React']
        }
        return render(request, "hello_world.html", context=data)
        
    