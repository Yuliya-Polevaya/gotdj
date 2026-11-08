# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserProfile
from .models import Person
from .models import Categorii
from .models import Product
from .forms import UserProfileForm



  
# def index(request):
#     peopl=Person.objects.get(pk=1)
#     peo=Person.objects.all()
#     print(peo)
#     people=peo.exclude(name='kvvh').order_by('-name')
#     print(people.query)
#     print(peo.values())
#     print(peo.values_list())
#     print(peopl.id)
#     print(peopl.name)
#     print(peopl.age)

#     context = {
#         "person": peopl,"people": people
#     }
#     return render(request, 'index.html',context=context)

def index(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = UserProfileForm()
    try:
        peopl = Person.objects.get(pk=1)
    except Person.DoesNotExist:
        peopl = None
        
    peo = Person.objects.all()
    people = peo.exclude(name='kvvh').order_by('-name')

    context = {
        "person": peopl,
        "people": people,
        "form": form, 
    }
    return render(request, 'index.html', context=context)


def news(request):
    return render(request, 'news.html')

def prod(request, pk=0):
    category = Categorii.objects.all()
    
    if pk == 0:
        product = Product.objects.all()
    else:
        product = Product.objects.filter(cat_id=pk) 
        
    info = {
        "category": category,
        "product": product
    }
    return render(request, "prod.html", context=info)

def blog(request):
    return render(request, 'blog.html')

def onas(request):
    return render(request, 'onas.html')

def form(request):
    return render(request, 'form.html', {"name": "", "email": ""})

def odr(request):
    if request.method == "POST":
        name = request.POST.get("name", "не найден")
        email = request.POST.get("email", "не найден")
        answer = request.POST.get("answer")
        site = request.POST.get("site")
        age = request.POST.get("age")
    else:
        return redirect('form')

    return render(request, 'odr.html', {
        "name": name, "email": email,
        "answer": answer, "site": site, "age": age,
    })

    
def prod(request, pk=0):
    category = Categorii.objects.all()
    product = Product.objects.select_related('cat_id').all()

    info = {
        "category": category,
        "product": product
    }

    return render(request, "prod.html", context=info)



# Create your views here.
