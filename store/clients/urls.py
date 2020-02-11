from django.urls import path
from . import views


urlpatterns = [
    path('',views.products, name="products"),     
    path('login/',views.login, name="login"),
    path('order/<int:product_id>/', views.product_detail, name="product_detail"), 
    path('create_order/', views.create_order, name="create_order"),
    path('update/<int:pk>/', views.update_order, name="update"), 
    path('delete/<int:pk>/', views.delete_order, name="delete"), 
]

#  <!-- <img class="card-img-top" src="{% static 'images/home.jpeg' %}" alt="Card image cap"> -->