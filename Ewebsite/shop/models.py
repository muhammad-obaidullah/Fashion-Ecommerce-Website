from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=3000)
    collection_name = models.CharField(max_length=100, default = "")
    image = models.ImageField(upload_to = "shop/images", default = "")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length = 100, default = "")
    phone = models.CharField(max_length = 100, default = "")
    desc = models.CharField(max_length=3000)

    def __str__(self):
        return self.name