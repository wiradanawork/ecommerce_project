from django.db import models

# Model Product mewakili item yang ada di toko e-commerce.
class Product(models.Model):
    
    # Field ini menyimpan nama produk. Menggunakan CharField, yang berarti ini adalah field teks dengan panjang maksimal 100 karakter.
    name = models.CharField(max_length=100)
    
    # Field ini menyimpan harga produk. Menggunakan IntegerField, yang berarti hanya angka bulat (integer) yang dapat digunakan sebagai harga.
    price = models.IntegerField()
    
    # Field ini menyimpan deskripsi produk. TextField digunakan di sini, yang memungkinkan untuk memasukkan teks panjang (lebih dari CharField).
    description = models.TextField()

    # Metode ini digunakan untuk menentukan apa yang ditampilkan ketika sebuah objek Product diwakili sebagai string.
    # Di sini, kita mengembalikan nama produk, yang membuatnya lebih mudah dikenali saat berinteraksi dengan objek ini di panel admin atau shell.
    def __str__(self):
        return self.name
