from django.db import models
from django.contrib.auth.models import User
from .managers import SubCategoryManager, CategoryManager
# Create your models here.

# class Product(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(max_length=200, null=True, blank=True)
#     image = models.ImageField(null=True, blank=True)
#     brand = models.CharField(max_length=200, null=True, blank=True)
#     category = models.CharField(max_length=100, null=True, blank=True)
#     description = models.TextField(max_length=200, null=True, blank=True)
#     rating = models.DecimalField(null=True, blank=True,max_digits=7, decimal_places=2)
#     numReviews = models.IntegerField(null=True, blank=True, default=0)
#     price = models.DecimalField(null=True, blank=True,max_digits=7, decimal_places=2)
#     countInStock = models.IntegerField(null=True, blank=True, default=0)
#     createdAt = models.DateField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)
#     def __str__(self):
#         return self.name
    

# class Review(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(max_length=200, null=True, blank=True)
#     rating = models.IntegerField(null=True, blank=True, default=0)
#     comment = models.TextField(null=True, blank=True)
#     createdAt = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.rating)

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     paymentMethod = models.CharField(max_length=200, null=True, blank=True)
#     taxPrice = models.DecimalField(
#         max_digits=7, decimal_places=2, null=True, blank=True)
#     shippingPrice = models.DecimalField(
#         max_digits=7, decimal_places=2, null=True, blank=True)
#     totalPrice = models.DecimalField(
#         max_digits=7, decimal_places=2, null=True, blank=True)
#     isPaid = models.BooleanField(default=False)
#     paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
#     isDelivered = models.BooleanField(default=False)
#     deliveredAt = models.DateTimeField(
#         auto_now_add=False, null=True, blank=True)
#     createdAt = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.createdAt)


# class OrderItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(max_length=200, null=True, blank=True)
#     qty = models.IntegerField(null=True, blank=True, default=0)
#     price = models.DecimalField(
#         max_digits=7, decimal_places=2, null=True, blank=True)
#     image = models.CharField(max_length=200, null=True, blank=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.name)


# class ShippingAddress(models.Model):
#     order = models.OneToOneField(
#         Order, on_delete=models.CASCADE, null=True, blank=True)
#     address = models.CharField(max_length=200, null=True, blank=True)
#     city = models.CharField(max_length=200, null=True, blank=True)
#     postalCode = models.CharField(max_length=200, null=True, blank=True)
#     country = models.CharField(max_length=200, null=True, blank=True)
#     shippingPrice = models.DecimalField(
#         max_digits=7, decimal_places=2, null=True, blank=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.address)


# class A(models.Model):
#     title = models.CharField(max_length=200, null=True, blank=True)
#     context = models.TextField(max_length=200, null=True, blank=True)
   

#     def __str__(self):
#         return str(self.title)
# class B(models.Model):
#     name = models.CharField(max_length=200, null=True, blank=True)
#     context = models.TextField(max_length=200, null=True, blank=True)
#     a = models.OneToOneField(A, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return str(self.name)


















# doodle works to implement recursive tree
class Node(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True )

    def __str__(self):
        return str(self.name)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Nodes'

# proxy model
class Category(Node):
    objects = CategoryManager()
    class Meta:
        proxy = True
        verbose_name_plural = 'Categories'

# proxy model sub-category
class SubCategory(Node):
    objects = SubCategoryManager()
    class Meta:
        proxy = True
        verbose_name_plural = 'Sub Categories'

# proxy model sub-s-category
# class SubSCategory(Node):
#     objects = SubSCategoryManager()
#     class Meta:
#         proxy = True
#         verbose_name_plural = 'Sub S Categories'

# sub-sub-category
class SubSubCategory(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True )
    name = models.CharField(max_length=155)

    def __str__(self):
        return str(self.name)







# class Category(models.Model):
#     _id = models.AutoField(primary_key=True, editable=False)
#     name = models.CharField(max_length=200, null=True, blank=True)
#     is_parent = models.CharField(max_length=200, null=True, blank=True)

#     parent_id = models.CharField(max_length=200, null=True, blank=True)

#     is_popular = models.CharField(max_length=200, null=True, blank=True)
#     status = models.CharField(max_length=200, null=True, blank=True)
    

#     def __str__(self):
#         return str(self.name)


