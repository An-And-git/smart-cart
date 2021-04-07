from django.urls import path, include
from product import views

urlpatterns = [
    path('', views.product, name='product'),
    path('<int:product_id>/', views.cart, name='cart')
]
