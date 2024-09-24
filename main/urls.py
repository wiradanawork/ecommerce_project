from django.urls import path
from .views import product_list, add_product, show_json, show_xml, show_json_by_id, show_xml_by_id, register, login_view, logout_view

urlpatterns = [
    path('', product_list, name='product_list'),
    path('products/add/', add_product, name='add_product'),
    path('products/json/', show_json, name='show_json'),
    path('products/xml/', show_xml, name='show_xml'),
    path('products/json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('products/xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
