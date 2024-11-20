from django.db import models
from django.contrib.auth.models import User

# Model Product mewakili item yang ada di toko e-commerce
class Product(models.Model):
    
    # Field ini menyimpan nama produk
    name = models.CharField(max_length=100)
    
    # Field ini menyimpan harga produk
    price = models.IntegerField()
    
    # Field ini menyimpan deskripsi produk
    description = models.TextField()
    
    # Setiap produk dikaitkan dengan pengguna yang menambahkannya
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # Metode ini mengembalikan nama produk sebagai representasi string
    def __str__(self):
        return self.name




    