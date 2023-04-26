from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def home_page(request):

    if request.method == "GET":
        all_categories  = Category.objects.all()
        mens_products = Product.objects.filter(category__name="MEN") #(category=2)
        womens_products = Product.objects.filter(category__name="WOMEN")
        kids_products = Product.objects.filter(category__name="KIDS")
        context = {
           "all_categories": all_categories,
           "mens_products": mens_products,
           "womens_products": womens_products,
           "kids_products": kids_products
        }
    elif request.method == "POST":
        new_subscribers_name = request.POST["name"] # or request.POST.get("name")
        new_subscribers_email = request.POST.get("email") #or request.POST["email"]
        subscribers.objects.create(name=new_subscribers_name, email=new_subscribers_email)
        return redirect("home")
        # return HttpResponse("You have subscribed Succcessfully")

    return render(request, "money/index.html", context)

def about(request):
    return render(request, "money/about.html")


def single_product_detail(request):
    return render(request, "money/single-product.html")
