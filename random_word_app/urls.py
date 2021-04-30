from django.urls import path
from . import views

urlpatterns = [
    path('', views.dom_word),
    path('random_word', views.dom_word),
    path('reset', views.reset)
]