from django.shortcuts import render
from .models import *
# Create your views here.

def home_page(request):
    
    all_categories  = Category.objects.all()
    context = {
        "all_categories": all_categories
    }
    return render(request, "money/index.html",context)