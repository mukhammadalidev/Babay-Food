from django.urls import path
from .views import CategoryCreateView,CategoryDeleteView,CategoryUpdateView,CategoryListAPIView

urlpatterns = [
    path('all/', CategoryListAPIView.as_view(), name='category_list'),
    path('create/', CategoryCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', CategoryDeleteView.as_view(), name='category'),
    path('<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
]