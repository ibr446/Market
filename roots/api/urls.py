from django.urls import path

from .views import RegisterAPIView, LoginAPIView, UserUpdateView, BrandAPI, CategoryAPI, ProductAPI

urlpatterns = [
    path("register", RegisterAPIView.as_view(), name="register"),
    path("user/<int:pk>/update", UserUpdateView.as_view(), name='user-update'),
    path("brand", BrandAPI.as_view(), name="brand"),
    path("category", CategoryAPI.as_view(), name="category"),
    path("product", ProductAPI.as_view(), name="product"),
    path("login", LoginAPIView.as_view(), name="login"),
]

