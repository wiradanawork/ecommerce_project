from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm

def product_list(request):
    data = {
        'nama': 'Muhammad Rayyan Wiradana',
        'npm': '2306275342',
        'kelas': 'c'
    }
    # Mengambil semua produk dari model Product
    products = Product.objects.all()
    
    return render(request, 'main/product_list.html', {'products': products, 'data': data})

# View untuk menampilkan semua produk dalam format JSON
def show_json(request):
    # Mengambil semua produk dari model Product
    products = Product.objects.all()

    # Reeturn data produk dalam format JSON
    return HttpResponse(serializers.serialize('json', products), content_type='application/json')

# View untuk menampilkan semua produk dalam format XML
def show_xml(request):
    # Mengambil semua produk dari model Product
    products = Product.objects.all()

    # Return data produk dalam format XML
    return HttpResponse(serializers.serialize('xml', products), content_type='application/xml')

# View untuk menampilkan produk berdasarkan id dalam format JSON
def show_json_by_id(request, id):
    # Mengambil satu produk berdasarkan ID saya pake get karena kalo pake filter pas dijalanin di postman error
    product = Product.objects.get(pk=id)

    # Mengembalikan data produk dalam format JSON
    return HttpResponse(serializers.serialize("json", [product]), content_type="application/json")

# View untuk menampilkan produk berdasarkan ID dalam format XML
def show_xml_by_id(request, id):
    # Mengambil satu produk berdasarkan ID saya pake get karena kalo pake filter pas dijalanin di postman error
    product = Product.objects.get(pk=id)
    
    # Mengembalikan data produk dalam format XML
    return HttpResponse(serializers.serialize("xml", [product]), content_type="application/xml")

# View untuk menambah produk baru
def add_product(request):
    # Jika metode HTTP adalah POST, memproses form
    if request.method == 'POST':
        form = ProductForm(request.POST)
        
        # Jika data form valid, simpan produk baru ke dalam database
        if form.is_valid():
            form.save()
            # Redirect ke halaman daftar produk setelah produk baru disimpan
            return redirect('product_list')
    else:
        # Jika metode bukan POST, buat form kosong untuk ditampilkan
        form = ProductForm()
    
    # Me-render template add_product.html dengan form produk
    return render(request, 'main/add_product.html', {'form': form})
