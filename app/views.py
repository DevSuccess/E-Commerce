from django.db.models import Count
from django.shortcuts import render
from django.views import View
from . import models


# Create your views here.
def home(request):
    return render(request, 'app/home.html')


class CategoryView(View):
    def get(self, request, val):
        products = models.Product.objects.filter(category=val)
        titles = models\
            .Product.objects.filter(category=val).values('title')
        return render(request, 'app/category.html', locals())
