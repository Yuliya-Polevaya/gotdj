from django.contrib import admin
from .models import Person, Categorii, Product, UserProfile

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "age")

@admin.register(Categorii)
class CategoriiAdmin(admin.ModelAdmin):
    list_display = ("title", "comment")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "sale", "material", "date_prod", "counter", "cat_id")

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "age")
# Register your models here.
