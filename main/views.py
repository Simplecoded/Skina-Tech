from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib import messages
from .models import Producto, Categoria, Subcategoria

# Create your views here.

def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={})

@login_required
def producto(request):
    return render (request=request,
                   template_name='main/productos.html',
                   context= {"Productos": Producto.objects.all})
@login_required
def categoria(request):
    return render (request=request,
                   template_name='main/categorias.html',
                   context= {"Categorias": Categoria.objects.all})
@login_required
def subcategoria(request):
    return render (request=request,
                   template_name='main/subcategorias.html',
                   context= {"Subcategoria": Subcategoria.objects.all})
@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")


def login_request(request):
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "main/login.html",
                  context={"form":form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})
@login_required
def account(request):
    return render(request= request,
                   template_name='main/account.html',
                   context = {})