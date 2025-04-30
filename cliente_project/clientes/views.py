from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

# LISTA CLIENTES


def lista_clientes(request):
    clientes = Cliente.objects.all()  # Obtener todos los clientes
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

# NUEVO CLIENTE


def nuevo_cliente(request):
    if request.method == 'POST':
        # Crear un formulario con los datos del POST
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el nuevo cliente en la base de datos
            # Redirigir a la lista de clientes
            return redirect('lista_clientes')
    else:
        form = ClienteForm()  # Crear un formulario vacío

    # Renderizar la plantilla con el formulario
    return render(request, 'clientes/nuevo_cliente.html', {'form': form})

# EDITAR CLIENTE


def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)  # Obtener el cliente por su ID
    if request.method == 'POST':
        # Crear un formulario con los datos del POST y el cliente existente
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()  # Guardar los cambios en el cliente
            # Redirigir a la lista de clientes
            return redirect('lista_clientes')
    else:
        # Crear un formulario con los datos del cliente
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/editar_cliente.html', {'form': form})  #

# ELIMINAR CLIENTE


def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)  # Obtener el cliente por su ID
    if request.method == 'POST':
        cliente.delete()  # Eliminar el cliente de la base de datos
        return redirect('lista_clientes')  # Redirigir a la lista de clientes
    return render(request, 'clientes/eliminar_cliente.html', {'cliente': cliente})


    



