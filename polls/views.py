from django.shortcuts import render, redirect, HttpResponse
from .models import BookList
from django.contrib import messages


# Create your views here.

def index(request):
    books = BookList.objects.all()
    return  render(request, 'index.html', {'books':books})

def editar(request, id):
    try:
        books = BookList.objects.get(pk=id)
        context = {
            'book':books
        }
        return render(request, 'editar.html', context)
    except:
        return redirect('/')
def eliminar(request, id):
    books = BookList.objects.get(pk=id)
    books.delete()
    messages.success(request, 'Se elimino correctamente!')
    return redirect('/')

def agregar(request):
    return render(request, 'agregar.html')

def actualizar(request, id):
    books = BookList.objects.get(pk=id)
    books.title = request.GET['title']
    books.price = request.GET['price']
    books.author = request.GET['author']
    books.save()
    messages.success(request, 'Se Actualizo correctamente!')
    return redirect('/')

def guardar(request):
    try:
        titulo = request.POST['titulo']
        precio = request.POST['precio']
        autor = request.POST['autor']
        new_book = BookList(title = titulo, price = int(precio), author = autor)
        new_book.save()
        messages.success(request, 'Libro guardado correctamente!')
        return redirect('/')
    except ValueError:
        messages.add_message(request, messages.WARNING, 'No se pueden insertar los datos, asegurate de llenar todos los campos o ingresar precios reales')
        return redirect('/')