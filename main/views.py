from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from .models import Product
from .forms import ProductForm, RegisterForm
from django.utils.timezone import localtime

# Fungsi untuk mendaftarkan pengguna baru
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Jika form valid, simpan data pengguna baru ke database
            form.save()
            # Redirect ke halaman login setelah pendaftaran berhasil
            return redirect('login')
    else:
        form = RegisterForm()
    # Render template register.html dengan form pendaftaran
    return render(request, 'main/register.html', {'form': form})

# Fungsi untuk login pengguna
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Mengambil username dan password dari form yang telah divalidasi
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Autentikasi pengguna berdasarkan username dan password
            user = authenticate(username=username, password=password)
            if user is not None:
                # Login pengguna jika autentikasi berhasil
                login(request, user)
                response = redirect('product_list')
                
                # Mengambil last_login dan mengubahnya ke waktu lokal
                last_login_time = localtime(user.last_login).strftime('%Y-%m-%d %H:%M:%S')
                # Menyimpan last_login dalam cookie
                response.set_cookie('last_login', last_login_time)
                return response
    else:
        form = AuthenticationForm()
    # Render template login.html dengan form login
    return render(request, 'main/login.html', {'form': form})

# Fungsi untuk logout pengguna
def logout_view(request):
    # Melakukan logout dan redirect ke halaman login
    logout(request)
    return redirect('login')

# View yang hanya bisa diakses oleh pengguna yang sudah login
@login_required
def product_list(request):
    data = {
        'nama': 'Muhammad Rayyan Wiradana',
        'npm': '2306275342',
        'kelas': 'c'
    }
    
    # Mengambil produk yang hanya dimiliki oleh pengguna yang sedang login
    products = Product.objects.filter(user=request.user)
    
    # Mengambil informasi last_login dari cookie
    last_login = request.COOKIES.get('last_login', 'First time')

    # Mengambil username pengguna yang sedang login
    username = request.user.username
    
    # Render template product_list.html dengan data produk, informasi pengguna, dan last_login
    return render(request, 'main/product_list.html', {'products': products, 'data': data, 'last_login': last_login, 'username': username})

# Fungsi untuk menambah produk baru
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Menyimpan produk baru dan menghubungkannya dengan pengguna yang sedang login
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            # Redirect ke halaman daftar produk setelah produk disimpan
            return redirect('product_list')
    else:
        form = ProductForm()
    # Render template add_product.html dengan form produk
    return render(request, 'main/add_product.html', {'form': form})

# View untuk menampilkan semua produk dalam format JSON
def show_json(request):
    products = Product.objects.all()
    # Mengembalikan data produk dalam format JSON
    return HttpResponse(serializers.serialize('json', products), content_type='application/json')

# View untuk menampilkan semua produk dalam format XML
def show_xml(request):
    products = Product.objects.all()
    # Mengembalikan data produk dalam format XML
    return HttpResponse(serializers.serialize('xml', products), content_type='application/xml')

# View untuk menampilkan produk berdasarkan ID dalam format JSON
def show_json_by_id(request, id):
    product = Product.objects.filter(pk=id)
    # Mengembalikan data produk dalam format JSON
    return HttpResponse(serializers.serialize("json", product), content_type="application/json")

# View untuk menampilkan produk berdasarkan ID dalam format XML
def show_xml_by_id(request, id):
    product = Product.objects.filter(pk=id)
    # Mengembalikan data produk dalam format XML
    return HttpResponse(serializers.serialize("xml", product), content_type="application/xml")
