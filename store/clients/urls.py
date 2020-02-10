from django.urls import path
from . import views


urlpatterns = [
    path('',views.products),     
    path('login/',views.login),
 
    path('order/<int:product_id>/', views.product_detail, name="product_detail"), 
   
]

#  <!-- <img class="card-img-top" src="{% static 'images/home.jpeg' %}" alt="Card image cap"> -->