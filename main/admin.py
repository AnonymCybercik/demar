from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Question)
admin.site.register(Contact)
admin.site.register(Order)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name',]
	list_display_links = ['name',]
	prepopulated_fields = {'slug':('name',)}
# Product
@admin.register(Product)
class ProAdmin(admin.ModelAdmin):
	list_display = ['name', 'category', 'instock']
	list_display_links = ['name', ]
	prepopulated_fields = {'slug':('name',)}

	class Meta:
		model = Product

@admin.register(Cart)
class Cart(admin.ModelAdmin):
	list_display = ['product', 'mkv', 'all_price']
	list_display_links = ['product', ]

@admin.register(MainCart)
class MainCart(admin.ModelAdmin):
	list_display = ['all_price']
	list_display_links = ['all_price', ]