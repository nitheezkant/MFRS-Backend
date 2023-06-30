from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name="home"),
    path('add-food',views.Addfood,name="add-food"),
    path('update-food/<str:pk>/',views.updatefood,name="update-food"),
    path('delete-food/<str:pk>/',views.deletefood,name="delete-food"),
    
    path('add-type',views.AddType,name="add-type"),
    path('update-type/<str:pk>/',views.updatetype,name="update-type"),
    path('delete-type/<str:pk>/',views.deletetype,name="delete-type"),

    path('food/<str:pk>/',views.food,name="food"),

    path("foodcom/",views.foodcom,name="foodcom"),
    path("foodcom/<str:date>/",views.dateView,name="mealDate"),
    path("foodcom/<str:date>/<str:meal>/",views.mealView,name="mealView")
]