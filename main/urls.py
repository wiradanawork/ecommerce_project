from django.urls import path
from .views import product_list, add_product, show_json, show_xml, show_json_by_id, show_xml_by_id, register, login_view, logout_view, product_edit, delete_product,create_product_ajax

urlpatterns = [
    path('', product_list, name='product_list'),
    path('products/add/', add_product, name='add_product'),
    path('product/<int:pk>/edit/', product_edit, name='product_edit'),
    path('products/delete/<int:id>/', delete_product, name='delete_product'),
    path('products/json/', show_json, name='show_json'),
    path('products/xml/', show_xml, name='show_xml'),
    path('products/json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('products/xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create-ajax/', create_product_ajax, name='create_product_ajax'),

]
