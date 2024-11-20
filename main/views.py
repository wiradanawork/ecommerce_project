from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from .models import Product
from .forms import ProductForm, RegisterForm
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Fungsi untuk mendaftarkan pengguna baru
from django.http import HttpResponse

@csrf_exempt
def register(request):
    if request.method == 'OPTIONS':
        # Tanggapi preflight request dengan izin metode
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            data = json.loads(request.body)
            form = RegisterForm(data)
            if form.is_valid():
                form.save()
                return JsonResponse({'status': 'success', 'message': 'User registered successfully'}, status=201)
            else:
                return JsonResponse({'status': 'failed', 'message': form.errors}, status=400)
    return JsonResponse({'status': 'failed', 'message': 'Invalid request method'}, status=405)



# Fungsi untuk login pengguna
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'success', 'message': 'Login successful'}, status=200)
            else:
                return JsonResponse({'status': 'failed', 'message': 'Invalid username or password'}, status=400)
        else:
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    response = redirect('product_list')
                    last_login_time = localtime(user.last_login).strftime('%Y-%m-%d %H:%M:%S')
                    response.set_cookie('last_login', last_login_time)
                    return response
    else:
        form = AuthenticationForm()
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

# Fungsi untuk mengedit produk
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Arahkan kembali ke daftar produk setelah berhasil
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'main/product_edit.html', {'form': form, 'product': product})

# Fungsi untuk menghapus produk
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    # Redirect ke halaman daftar produk setelah menghapus
    return redirect('product_list')

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
@login_required
def show_json(request):
    products = Product.objects.filter(user=request.user)
    data = serializers.serialize('json', products)
    return JsonResponse(data, safe=False)

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
    
@csrf_exempt
@login_required
def create_product_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = ProductForm(data)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return JsonResponse({
                'status': 'success',
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'description': product.description
                }
            }, status=201)
        else:
            return JsonResponse({'status': 'failed', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'failed', 'message': 'Invalid request method'}, status=405)
