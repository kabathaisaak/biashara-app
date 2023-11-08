from django.shortcuts import render, redirect
from biasharaapp.models import Member, Products
from biasharaapp.forms import ProductsForm

# Create your views here.

from django.contrib.auth.models import User  # Use the appropriate User model in your project


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        new_member = Member(username=username)
        new_member.password = password

        new_member.save()

        return redirect('/')

    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'index.html', {'Member': Member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def inner(request):
    return render(request, 'inner-page.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def department(request):
    return render(request, 'department.html')


def doctors(request):
    return render(request, 'doctors.html')


def add(request):
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save
            return redirect("/")
    else:
        form = ProductsForm()
        return render(request, 'addproduct.html', {'form': form})


def show(request):
    Product = Products.objects.all()

    return render(request, 'show.html', {'Product': Product})


def delete(request, id):
    product = Products.objects.get(id=id)
    product.delete()
    return redirect('/show')


def edit(request, id):
    product = Products.objects.get(id=id)
    return render(request, 'edit.html', {'product': product})


def update(request, id):
    product = Products.objects.get(id=id)
    form = ProductsForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html', {'product': product})
