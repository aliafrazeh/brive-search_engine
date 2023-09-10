from django.urls import path
from .views import home,search,license_view,programmer


app_name = "pages"
urlpatterns = [
    path('',home,name="home"),
    path('search/',search,name="search"),
    path('license/',license_view,name="license"),
    path('developer/',programmer,name="programmer")
]