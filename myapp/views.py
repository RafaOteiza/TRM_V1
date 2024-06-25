from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Usuario
from .forms import UsuarioForm



def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente.')
    return redirect('login')

def index(request):
    user = request.user
    context = {'user': user}
    return render(request, 'myapp/index.html', context)

def index(request):
    return render(request, 'myapp/index.html')

def alineacion(request):
    return render(request, 'myapp/alineacion.html')

def frenos(request):
    return render(request, 'myapp/frenos.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        usuario = authenticate(request, email=email, password=password)
        if usuario is not None:
            login(request, usuario)
            messages.success(request, f'Bienvenido {usuario.nombre}')
            return redirect('index')
        else:
            messages.error(request, 'Correo o contraseña incorrectos.')
    return render(request, 'myapp/login.html')

def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('login')
    else:
        form = UsuarioForm()
    return render(request, 'myapp/registro.html', {'form': form})

def usuario(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        usuario = Usuario.objects.get(id=usuario_id)
        return render(request, 'myapp/usuario.html', {'usuario': usuario})
    return redirect('login')

def cart_view(request):
    return render(request, 'myapp/cart.html')


def motor(request):
    return render(request, 'myapp/motor.html')

def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'myapp/usuario_list.html', {'usuarios': usuarios})

def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm()
    return render(request, 'myapp/usuario_form.html', {'form': form})

def usuario_update(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'myapp/usuario_form.html', {'form': form})

def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'myapp/usuario_confirm_delete.html', {'usuario': usuario})

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'myapp/usuario_list.html', {'usuarios': usuarios})
