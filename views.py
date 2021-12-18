from django.shortcuts import render

menu = [{"item":"მთავარი", "href":"home","id":1},
        {"item":"კონტაქტი", "href":"contact","id":2}]

# Create your views here.
def index(request):
    
    return render(request, 'main/index.html' ,{'menu':menu, "id":1})

def contact(request):
    
    return render(request, 'main/contact.html' ,{'menu':menu,"id":2})
    