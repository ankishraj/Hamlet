from django.urls import path
from Accounts import admin
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<int:req_id>', views.customer, name="customer"),
    path('order_now/', views.create_order, name="create_order"),
    path('update_order/<int:order_id>', views.update_order, name="update_order"),
    path('del_order/<int:order_id>', views.delete_order, name="delete_order")
]
