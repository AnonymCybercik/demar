from multiprocessing import context
from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from django.contrib import messages
from django.template import RequestContext
from django.http import JsonResponse, request
from django.contrib.auth.models import User

def index(request):
	products = Product.objects.all().order_by('-id')
	if request.method == 'POST':
		name = request.POST['name']
		phone = request.POST['phone']
		message = request.POST['message']
		Question.objects.create(name=name,phone=phone,message=message)	
	return render(request,'index.html',{'products':products})

def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		phone = request.POST['phone']
		email = request.POST['email']
		Contact.objects.create(name=name,phone=phone,email=email)	
	return render(request,'contact.html')

def cart(request):
	
	main = request.session['cart']
	cart = get_object_or_404(MainCart, id=int(main))
	context = {
		'cart':cart,
	}
	return render(request,'cart.html', context)

def plitki(request):
	products = Product.objects.all().order_by('-id')
	return render(request,'catalogStone.html',{'products':products})

def laminat(request):
	products = Product.objects.all().order_by('-id')
	return render(request,'catalogLaminat.html',{'products':products})

def gallery(request):
	return render(request,'gallery.html')

# cart block

def mainCartCreate(request):
	try:
		print(request.session['cart'])
	except:
		cart = MainCart.objects.create()
		request.session['cart'] = cart.id
		print('cart created')

	return request


def cart_create(request):
	main = request.session['cart']
	product_id = request.GET.get('product_id')
	mkv = request.GET.get('mkv')
	product = Product.objects.get(id=product_id)
	all_price = float(mkv)*float(product.price)
	new = Cart.objects.create(
		product=product,
		mkv=float(mkv),
		all_price=all_price
	)
	mainCart = MainCart.objects.get(id=main)
	if new not in mainCart.carts.all():
		mainCart.carts.add(new)
		a = 0.0
		for i in mainCart.carts.all():
			a += i.all_price
		mainCart.all_price = a
		mainCart.save()
	return JsonResponse({'data':'created'})

def cart_update(request):
	main = request.session['cart']
	mkv = request.GET.get('mkv')
	cart_id = request.GET.get('cart_id')
	cart = Cart.objects.get(id=int(cart_id))
	price = cart.product.price*float(mkv)
	cart.all_price = price
	cart.mkv = mkv
	cart.save()
	mainCart = MainCart.objects.get(id=main)
	a = 0.0
	for i in mainCart.carts.all():
		a += i.all_price
	mainCart.all_price = a
	mainCart.save()
	return JsonResponse({
		'price':cart.all_price,
		'main_price':mainCart.all_price
		})

def cart_delete(request):
	main = request.session['cart']
	cart_id = request.GET.get('cart_id')
	cart = Cart.objects.get(id=int(cart_id))
	cart.delete()
	mainCart = MainCart.objects.get(id=main)
	a = 0.0
	for i in mainCart.carts.all():
		a += i.all_price
	mainCart.all_price = a
	mainCart.save()
	return JsonResponse({'main_price':mainCart.all_price})

import telebot
TOKEN = '5189245732:AAHLRbxCGDZmrZZtUQaEgPWQTcuSS3IACGQ'
chat_id = 696007117
tb = telebot.TeleBot(TOKEN)


def order(request):
	main = request.session['cart']
	mainCart = MainCart.objects.get(id=main)
	name = request.GET.get('name')
	surname = request.GET.get('surname')
	phone = request.GET.get('phone')
	if mainCart.carts:
		order = Order.objects.create(
			first_name=name,
			last_name=surname,
			phone=int(phone),
			cart=mainCart
		)
		message = f"Ismi: {order.first_name}\nFamiliyasi: {order.last_name}\nTelefon raqami: {order.phone}\nTovarlar: \n"
		for i in order.cart.carts.all():
			message += f"{i}m kvadrat\n"
		message += f"Jami narxi: {order.cart.all_price} so'm"
		tb.send_message(chat_id, message)
	return redirect('/orderview/')


def orderView(request):
	return render(request, 'order.html')