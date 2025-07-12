from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from .models import *

from django.contrib.auth.mixins import LoginRequiredMixin



class HomeView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request,  'sections.html')

class ProductsView(LoginRequiredMixin,View):
    def get(self, request):
        products = Product.objects.filter(branch=request.user.branch).order_by('name')
        context = {
            'products': products
        }
        return render(request, 'products.html', context)

    def post(self, request):
        Product.objects.create(
            name=request.POST.get('name'),
            brand=request.POST.get('brand') if request.POST.get('brand') !="" else None,
            import_price=request.POST.get('import_price'),
            export_price=request.POST.get('export_price') if request.POST.get('export_price') !="" else None,
            amount=request.POST.get('amount'),
            unit=request.POST.get('unit'),
            updated_at=datetime.now(),
            branch=request.user.branch,
        )
        return self.get(request)

class ProductEditView(LoginRequiredMixin,View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk, branch=request.user.branch)
        context = {
            'product': product,
        }
        return render(request, 'product-edit.html', context)

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk, branch=request.user.branch)
        product.name = request.POST.get('name')
        product.brand = request.POST.get('brand')
        product.import_price = request.POST.get('import_price')
        product.export_price = request.POST.get('export_price')
        product.amount = request.POST.get('amount')
        product.unit = request.POST.get('unit')
        product.updated_at = datetime.now()
        product.branch=request.user.branch
        product.save()
        return redirect('products')

class ProductDeleteView(View):
    def get(self, request, pk):
        if request.is_authenticated:
           product = get_object_or_404(Product, pk=pk, branch=request.user.branch)
           context = {
             'product': product
           }
           return render(request, 'product-delete.html', context)
        return redirect('login')

    def post(self, request, pk):
        if request.is_authenticated:
         product = get_object_or_404(Product, pk=pk, branch=request.user.branch)
         product.delete()
         return redirect('products')
        return redirect('login')

class CustomerView(View):
    def get(self, request):
        customer = Customer.objects.filter(branch=request.user.branch).order_by('name')
        context = {
            'customer': customer,
        }
        return render(request, 'customer.html', context)

    def post(self):
        pass
