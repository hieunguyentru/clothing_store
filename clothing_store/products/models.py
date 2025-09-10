from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200) #Tên sản phẩm
    price = models.DecimalField(max_digits=10, decimal_places=2)#Giá sản phẩm
    description = models.TextField(blank= True) #Mô tả sản phẩm
    image = models.ImageField(upload_to='products/', blank=True, null=True) #Hình ảnh sản phẩm

    def __str__(self):
        return self.name