from django.contrib import admin
from .models import (User, Product, Comment,
                     Category, Brand, Order, Address)


admin.site.register(User)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Order)
admin.site.register(Address)




