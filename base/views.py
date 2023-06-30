from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Food,Meal,Type
from .forms import FoodForm,TypeForm
from django.http import HttpResponse
# Create your views here.

def home(request):
    q=request.GET.get('q') if request.GET.get('q')!=None else ''
    foods=Food.objects.filter(
        Q(type__name__icontains=q) |
        Q(name__icontains=q) 
     )
    dishescount=foods.count()
    types=Type.objects.all()
    context={'foods':foods,'types':types,'dishescount':dishescount}
    return render(request,'home.html',context)

def Addfood(request):
    form = FoodForm()
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'foodform.html',context)

def AddType(request):
    form = TypeForm()
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'typeform.html',context)

def updatefood(request,pk):
    food=Food.objects.get(id=pk)
    form=FoodForm(instance=food)
    if request.method =='POST':
        form = FoodForm(request.POST,instance=food)
        if form.is_valid():
            form.save() 
            return redirect('home')
    context={'form':form}
    return render (request,'foodform.html',context)

def updatetype(request,pk):
    type=Type.objects.get(id=pk)
    form=TypeForm(instance=type)
    if request.method =='POST':
        form = TypeForm(request.POST,instance=type)
        if form.is_valid():
            form.save() 
            return redirect('home')
    context={'form':form}
    return render (request,'typeform.html',context)

def deletefood(request,pk):
    food=Food.objects.get(id=pk)
    if request.method=='POST': 
        food.delete() 
        return redirect('home')
    return render(request,'deletefood.html',{'obj':food})

def deletetype(request,pk):
    type=Type.objects.get(id=pk)
    if request.method=='POST': 
        type.delete() 
        return redirect('home')
    return render(request,'deletetype.html',{'obj':type})

def food(request):
    pass

def foodcom(request):
    if request.method=='POST':
        date=request.POST.get('date')
        
        return redirect('mealDate',date=date)
    return render(request,"index.html")

def dateView(request,date):
    context={'date':date}
    if request.method=="POST":
        return redirect('mealView',date=date,meal=request.POST.get('type'))

    context={'date':date}
    return render(request,"date.html")

def mealView(request,date,meal):
    context={'date':date,'meal':meal}
    if request.method=="POST":
        food=request.POST.get('food')
        print(food)

    return render(request,"meal.html",context)
