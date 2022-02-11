from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.index, name='index'),
    path('contact/',views.contact,name='contact'),
    path('plitki/',views.plitki,name='plitki'),
    path('gallery/',views.gallery,name='gallery'),
    path('cart/',views.cart,name='cart'),
    path('laminat/',views.laminat,name='laminat'),
    path('cart-create/',views.cart_create,name='cart_create'),
    path('cart-update/',views.cart_update,name='cart_update'),
    path('cart-delete/',views.cart_delete,name='cart_delete'),
    path("order/", views.order, name="order"),
    path("orderview/", views.orderView, name="orderview"),
]