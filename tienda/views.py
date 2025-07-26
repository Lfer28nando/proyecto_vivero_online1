from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria

def home(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    q = request.GET.get('q')
    cat = request.GET.get('cat')
    if q:
        productos = productos.filter(nombre__icontains=q)
    if cat:
        productos = productos.filter(categoria_id=cat)
    return render(request, 'home.html', {
        'productos': productos,
        'categorias': categorias
    })

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'detalle.html', {'producto': producto})
