from django.urls import path
from .views import home , UpdatePost , DeletePost

urlpatterns = [
    path('',home,name="home"),
    path('update-post/<str:pk>/',UpdatePost,name="update-post"),
    path('delete-post/<str:pk>/',DeletePost,name="delete-post"),
]