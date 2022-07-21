from django.shortcuts import render, redirect
from django.views import View
from sklep.models import Product, Cart
from twitter_app.models import User


class ProductListView(View):

    def get(self, request):
        products = Product.objects.all()
        return render(request, 'sklep/product_list.html',
                      {'products':products})


class AddProductToCart(View):

    def get(self, request, product_id):
        user_id = request.session.get('user_id')
        print(user_id)
        if user_id is None:
            return redirect('login')
        user = User.objects.get(pk=user_id)
        product = Product.objects.get(pk=product_id)
        cart, created = Cart.objects.get_or_create(user=user, product=product)
        if not created:
            cart.amount += 1
            cart.save()
        return redirect('product_list')


class CartView(View):

    def get(self, request):
        user_id = request.session.get('user_id')
        if user_id is None:
            return redirect('login')
        user = User.objects.get(pk=user_id)
        return render(request, 'sklep/cart.html', {'user':user})


