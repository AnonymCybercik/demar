from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	name = models.CharField('Ismi',max_length=250,)
	phone = models.CharField('Telefon ', max_length=50)
	message = models.CharField('Xabari', max_length=250)

	class Meta:
		verbose_name = 'Savol'
		verbose_name_plural = 'Savollar'

	def __str__(self):
		return f"{self.name}"
class Contact(models.Model):
	name = models.CharField('Ismi',max_length=250,)
	phone = models.CharField('Telefon ', max_length=50)
	email = models.EmailField('Emaili', max_length=250)

	class Meta:
		verbose_name = 'Aloqa'
		verbose_name_plural = 'Aloqalar'

	def __str__(self):
		return f"{self.name}"


class Category(models.Model):
    name = models.CharField('Nomi',max_length=150,)
    slug = models.SlugField('*',max_length=150, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category_detail', kwargs={'category_slug':self.slug})

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='product_images/',blank=True)
    description = models.TextField(blank=True)
    price = models.FloatField()
    old_price = models.PositiveIntegerField('Avvalgi Narxi',default=0)
    available = models.BooleanField(default=True)
    instock = models.BooleanField('Bor / Yok', default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail',args=[str(self.slug)])


class Cart(models.Model):
    product = models.ForeignKey("main.Product", verbose_name="cart of product", on_delete=models.CASCADE)
    mkv = models.FloatField("m kvadrat")
    all_price = models.FloatField()

    def __str__(self):
        return f"{self.product.name}, --{self.mkv}"


class MainCart(models.Model):
    carts =  models.ManyToManyField(Cart, verbose_name="carts", blank=True)
    all_price = models.FloatField(default=0)

    def __str__(self):
        return str(self.carts.all().count())


class Order(models.Model):
    first_name = models.CharField("Ismi", max_length=50)
    last_name = models.CharField("familiyasi", max_length=50)
    phone = models.PositiveIntegerField("phone")
    cart = models.ForeignKey(MainCart, verbose_name="carts", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"