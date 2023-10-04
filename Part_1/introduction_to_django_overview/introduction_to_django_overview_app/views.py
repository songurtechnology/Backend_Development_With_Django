from django.shortcuts import render, get_object_or_404
from .models import Product

def year_archive(request, year):
    post_list = Product.objects.filter(share_date__year=year)
    return render(request, "year_archive.html", {"year": year, "post_list": post_list})

def month_archive(request, year, month):
    post_list = Product.objects.filter(share_date__year=year, share_date__month=month)
    return render(request, "month_archive.html", {"year": year, "month": month, "post_list": post_list})

def post_detail(request, year, month, pk):
    post = get_object_or_404(Product, share_date__year=year, share_date__month=month, pk=pk)
    return render(request, "post_detail.html", {"post": post})
