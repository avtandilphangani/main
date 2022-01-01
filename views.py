from django.shortcuts import render

menu = [{"item":"მთავარი", "href":"home","id":1},
        {"item":"კონტაქტი", "href":"contact","id":2}]

slides = [ {"img":"photo.jpg", "dark":"uk-light", "title":"თანამედროვე სახლის მოდელი", "button":"შეიტყვე მეტი", "text":"ძალიან ლამაზი ფოტოა, ხოლო ტექსტი ანიმირდება სურათთან ერთად"},
         {"img":"light.jpg", "dark":"uk-dark", "title":"ნათელი ფერების დიდზაინი","button":"ფერების შესახებ", "text":"ტექსტი ანიმრდება და მოცემულია შრიფტით გლახო"},
         {"img":"dark.jpg", "dark":"uk-light", "title":"მუქი სურათი","button":"ლამაზი ნაკეთობები", "text":"ტყავის ლამაზი ნაკეთობა"}]

# Create your views here.
def index(request):
    
    context = {'menu':menu,
               'slides':slides,
               'id':menu[0]["id"]
            
    }
    return render(request, 'main/index.html' ,context=context)

def contact(request):
    context = {'menu':menu,
               
               'id':menu[1]["id"]
    }
    return render(request, 'main/contact.html' ,context=context)

    