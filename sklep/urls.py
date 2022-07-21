
from django.urls import path
from sklep import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('add_product_to_cart/<int:product_id>/', views.AddProductToCart.as_view(), name='add_to_cart'),
    path('cart_view', views.CartView.as_view(), name='cart_view'),
]
