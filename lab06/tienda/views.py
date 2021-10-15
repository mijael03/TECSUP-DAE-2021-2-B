from django.shortcuts import get_object_or_404, redirect,render
from .models import Producto,Categoria,Pedido
from tienda.carrito import Cart
# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categories = Categoria.objects.all
    context = {
        'product_list': product_list,
        'categories': categories
        }
    return render(request,'index.html',context)

def producto(request,producto_id):
    producto = get_object_or_404(Producto,pk=producto_id)
    return render(request,'producto.html',{'producto':producto})

def CategoryView(request, cats):
    category_products = Producto.objects.filter(categoria=cats)
    return render(request, 'categories.html', { 'category_products':category_products})

def agregarCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def eliminarProductoCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.remove(objProducto)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def limpiarCarrito(request):
    CarritoProducto = Cart(request)
    CarritoProducto.clear()
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def carrito(request):
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def purchase(request):
    facture=request.session.get("cart")
    pedido=Pedido(factura=facture)
    pedido.save()
    return redirect('tienda:index')
