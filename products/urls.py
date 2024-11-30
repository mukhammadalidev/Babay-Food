from django.urls import path
from .views import ProductAPIView,ProductDetailAPIView,ProductCreateAPIView,ProductUpdateAPIView,ProductDeleteAPIView

urlpatterns = [
    path('all/',ProductAPIView.as_view(),name='all'),
    path('<int:pk>',ProductDetailAPIView.as_view(),name='detail'),
    path('create/',ProductCreateAPIView.as_view(),name='create'),
    path('<int:pk>/update/',ProductUpdateAPIView.as_view(),name='update'),
    path('<int:pk>/delete/',ProductDeleteAPIView.as_view(),name='delete'),

]