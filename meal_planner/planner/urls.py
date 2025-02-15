from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate_meal_plan/', views.generate_meal_plan, name='generate_meal_plan'),
]

#login
from django.urls import path
from allauth.account.views import LoginView
from . import views

urlpatterns = [
    path('', LoginView.as_view(), name='account_login'),
    path('generate/', views.generate_meal_plan, name='generate_meal_plan'),
    path('home/', views.home, name='home'),
     path('generate/', views.generate_meal_plan, name='generate_meal_plan'),

]
from django.urls import path
from allauth.account.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate_meal_plan, name='generate_meal_plan'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('recommend/', views.recommend_recipes, name='recommend_recipes'),
]

#ml train

