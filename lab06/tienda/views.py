from django.shortcuts import get_object_or_404,render
from .models import Producto,Categoria
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
    category_products = Producto.objects.filter(pk=cats)
    return render(request, 'categories.html', { 'category_products':category_products})