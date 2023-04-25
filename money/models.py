from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="category_images")


    class Meta:
      verbose_name_plural = "Categories"


    def __str__(self):
        return self.name
    


class Product(models.Model):
   name = models.CharField(max_length=100)
   description = models.TextField()
   price = models.DecimalField(max_digits=10, decimal_places=2)
   category = models.ForeignKey(Category,on_delete=models.CASCADE)
   image = models.ImageField(upload_to="product_images")


   def __str__(self):
      return self.name