from django.urls import path
from . import views

urlpatterns = [
    path('check/<start>/<end>/', views.check_num, name='check_prime_binary'),
]
