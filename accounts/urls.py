from django.urls import path
from .views import account_main

app_name = "account"
urlpatterns = [
    path('',account_main,name="account_home")
]
