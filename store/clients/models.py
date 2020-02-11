from django.db import models

class Products(models.Model):
    products_name = models.CharField(max_length=200)
    # product_image = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.FloatField(null=True,)
    objects = models.Manager()
    
    def __str__(self):
        return self.products_name

        
# class Books(models.Model):
#     # title = models.ForeignKey(Products, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     # title = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
#     author = models.CharField(max_length=200)

    
#     def __str__(self):
#         return self.title

