from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product

# Form untuk model product, digunakan saat menambah produk
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

# Form untuk registrasi user baru
# Menggunakan UserCreationForm bawaan Django untuk membuat form registrasi
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
