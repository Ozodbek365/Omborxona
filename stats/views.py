from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


class SalesView(LoginRequiredMixin,View):
    def get(self, request):
        sales = Sale.objects.filter(branch=request.user.branch).order_by('-date')
        context = {
            'sales': sales
        }
        return render(request, 'sales.html', context)