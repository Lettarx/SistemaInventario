
from django.contrib import admin
from django.urls import path
from InventarioAPP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login),
    path('inicio/',views.inicio),
    path('productos/', views.productos),
    path('addproducto/', views.addProducto),
    path('eliminarProducto/<int:id>',views.eliminarProducto),
    path('actualizarProducto/<int:id>',views.actualizarProducto),
]
