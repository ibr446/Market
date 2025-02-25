from django.urls import path

from .views import (RegisterAPIView, LoginAPIView,
                    UserUpdateView, BrandAPI, CategoryAPI,
                    ProductAPI, CommentListAPIView,
                    CommentDetailView, AddressDetailAPIView,
                    AddressListCreateAPIView, OrderListView, OrderDetailView, DealAPIView)


urlpatterns = [
    path("register", RegisterAPIView.as_view(), name="register"),
    path("user/<int:pk>/update", UserUpdateView.as_view(), name='user-update'),
    path("brand", BrandAPI.as_view(), name="brand"),
    path("category", CategoryAPI.as_view(), name="category"),
    path("product", ProductAPI.as_view(), name="product"),
    path("login", LoginAPIView.as_view(), name="login"),
    path('comments', CommentListAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('addresses/', AddressListCreateAPIView.as_view(), name='address-list-create'),
    path('addresses/<int:pk>/', AddressDetailAPIView.as_view(), name='address-detail'),
    path('orders', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='orders-detail'),
    path('deal', DealAPIView.as_view(), name='deal-list')
]







