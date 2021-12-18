from django.shortcuts import render

menu = [{"item":"მთავარი", "href":"home","id":1},
        {"item":"კონტაქტი", "href":"contact","id":2}]

# Create your views here.
def index(request):
    id = menu[0]["id"]
    return render(request, 'main/index.html' ,{'menu':menu, "id":id})

def contact(request):
    id = menu[1]["id"]
    return render(request, 'main/contact.html' ,{'menu':menu,"id":id})
    