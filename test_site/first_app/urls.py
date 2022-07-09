from django.urls import path

from .views import index, second_function

urlpatterns = [
    path('', index),
    path('second_page/', second_function)
]