from django.db import models

# Model Product mewakili item yang ada di toko e-commerce.
class Product(models.Model):
    
    # Field ini menyimpan nama produk. Menggunakan CharField, yang berarti ini adalah field teks dengan panjang maksimal 100 karakter.
    name = models.CharField(max_length=100)
    
    # Field ini menyimpan harga produk menggunakan integerField
    price = models.IntegerField()
    
    # Field ini menyimpan deskripsi produk, textField digunakan di sini, yang memungkinkan untuk memasukkan teks panjang (lebih dari CharField).
    description = models.TextField()

    # Metode ini digunakan untuk menentukan apa yang ditampilkan ketika sebuah objek Product diwakili sebagai string.
    # Kita mengembalikan nama produk.
    def __str__(self):
        return self.name
