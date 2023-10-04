from django.shortcuts import render, get_object_or_404
from .models import Product

def year_archive(request, year):
    p_list = Product.objects.filter(share_date__year=year)
    relation = {"year": year, "post_list": p_list}
    return render(request, "introduction_to_django_overview_app/year_archive.html", relation)

def month_archive(request, year, month):
    p_list = Product.objects.filter(share_date__year=year, share_date__month=month)
    relation = {"year": year, "month": month, "post_list": p_list}
    return render(request, "introduction_to_django_overview_app/month_archive.html", relation)


def post_detail(request, year, month, pk):
    post = get_object_or_404(Product, share_date__year=year, share_date__month=month, pk=pk)
    return render(request, "introduction_to_django_overview_app/post_detail.html", {"post": post})