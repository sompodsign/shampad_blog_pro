from django.urls import path
from . import views

app_name = 'amazon'

urlpatterns = [
    path('amazon/', views.price_tracker, name='amazon_price_tracker')
]