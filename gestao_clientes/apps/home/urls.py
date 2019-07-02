from django.urls import path
from .views import home, my_logout, HomePageTemplateView, MyView

urlpatterns = [
    path('', home, name="home"),
    path('logout/', my_logout, name="logout"),
    path('home2/', HomePageTemplateView.as_view(), name="logout"),
    path('home3/', MyView.as_view(), name="home3"),
]


