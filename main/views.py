from django.shortcuts import render

def product_list(request):
    # Daftar produk dan nama
    data = {
        'nama': 'Muhammad Rayyan Wiradana',
        'npm': '2306275342',
        'kelas':"c"
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
    
    
    return render(request, 'main/product_list.html', {'products': products, 'data': data})
