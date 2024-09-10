from django.shortcuts import render

def product_list(request):
    # Buat daftar produk secara manual tanpa database
    data = {
        'nama': 'Muhammad Rayyan Wiradana',
        'npm': '2306275342'
    }
    
    products = [
        {
            'name': 'Chitato',
            'description': 'Ini adalah makanan enak kripik kentang',
            'price': 10000,
        },
        {
            'name': 'Lays',
            'description': 'Kripik kentang rasa original',
            'price': 8000,
        }
    ]
    
    # Tambahkan data ke context bersama dengan products
    return render(request, 'main/product_list.html', {'products': products, 'data': data})
