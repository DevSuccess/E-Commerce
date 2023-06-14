from django.db.models import Count
from django.shortcuts import render
from django.views import View
from django.contrib import messages
from . import models
from . import forms


# Create your views here.
def home(request):
    return render(request, 'app/home.html')


def about(request):
    return render(request, 'app/about.html')


def contact(request):
    return render(request, 'app/contact.html')


class CategoryView(View):
    def get(self, request, val):
        products = models.Product.objects.filter(category=val)
        titles = models \
            .Product.objects.filter(category=val).values('title')
        return render(request, 'app/category.html', locals())


class CategoryTitle(View):
    def get(self, request, val):
        products = models.Product.objects.filter(title=val)
        titles = models.Product.objects \
            .filter(category=products[0].category) \
            .values('title')
        return render(request, 'app/category.html', locals())


class ProductDetail(View):
    def get(self, request, id):
        product = models.Product.objects.get(pk=id)
        return render(request, 'app/product_detail.html', locals())


class CustomerRegistrationView(View):
    def get(self, request):
        form = forms.CustomerRegistration()
        return render(request, 'app/customer_registration.html', locals())

    def post(self, request):
        form = forms.CustomerRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations ! User Register Successfully")
        else:
            messages.warning(request, "Invalid Input Data")

        return render(request, 'app/customer_registration.html', locals())