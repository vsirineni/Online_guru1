from django.db import models
from Hobbies.models import Inclass
from User.models import User


class CartItem(models.Model):
    classes = models.OneToOneField(Inclass, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.classes.class_name


class Cart(models.Model):
    ref_code = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(CartItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def __str__(self):
        return '{0}'.format(self.user)