from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

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
        return redirect("about")
    return render(request, "money/about.html")


def single_product_detail(request, id):
    myproduct = Product.objects.get(id=id)
    context = {
        "myproduct": myproduct
    }
    return render(request, "money/single-product.html", context)

def products_page(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "money/products.html", context)



def Contact_page(request):
    
    if request.method == "GET":
        form = ContactForm()
    elif request.method == "POST":
       
        form = ContactForm(request.POST)
        if form.is_valid(): 
          form.save()
        #   contact_name = form.cleaned_data["name"]
        #   contact_email = form.cleaned_data["email"]
        #   contact_subject = form.cleaned_data["subject"]
        #   contact_message = form.cleaned_data["message"]

        #   Contact.objects.create(name=contact_name, email=contact_email, subject=contact_subject, message=contact_message)
          return redirect("contactt")
    context = {
    "form": form
    }
    
    return render(request, "money/contact2.html", context)