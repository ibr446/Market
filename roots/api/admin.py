from django.contrib import admin
from .models import (User, Product, Comment,
                     Category, Brand, Order, Address, Deal)


admin.site.register(User)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(Deal)
# admin.site.register(Brand)

@admin.register(Brand)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name"]








