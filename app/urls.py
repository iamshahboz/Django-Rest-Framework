from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # path('product/', views.product_alt_view),
    # path('<int:pk>/', views.product_alt_view)


]