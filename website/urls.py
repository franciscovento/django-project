from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('vote/<int:convention_id>/', views.vote),
    path('members/', views.members),
    path('members/<int:member_id>/', views.member),
    path('conventions/', views.conventions),
    path('conventions/<int:convention_id>/', views.convention),
    ] 