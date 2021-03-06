from django.urls import path

from . import views

app_name = "userAccount"

urlpatterns = [
    path('register', views.register_request, name='register_request'),
    path('login', views.login_request, name='login_request'),
    path('logout', views.logout_request, name='logout_request'),
    path('orders', views.userOrders, name='user_orders')
]