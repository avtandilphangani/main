from django.shortcuts import render

menu = [{"item":"მთავარი", "href":"home","id":0},
        {"item":"კონტაქტი", "href":"contact","id":1}]

# Create your views here.
def index(request):
    
    return render(request, 'main/index.html' ,{'menu':menu})

def contact(request):
    
    return render(request, 'main/contact.html' ,{'menu':menu})
    