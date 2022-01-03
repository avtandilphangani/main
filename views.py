from django.shortcuts import render

from main.models import MainMenu


menu = MainMenu.objects.all()


# Create your views here.
def index(request):
    
    context = {'menu':menu,
               'slides':slides,
               'id':1
            
    }
    return render(request, 'main/index.html' ,context=context)

def contact(request):
    context = {'menu':menu,
               
               'id':2
    }
    return render(request, 'main/contact.html' ,context=context)

def gallery(request):
    return render(request, 'main/contact.html')
