from django.urls import path
from .views import *


urlpatterns = [
    path("", home_page, name="home"),
    path("about/", about, name="about"),
    path("<int:id>/", single_product_detail, name="single"),
    path("products/", products_page, name="products"),
]