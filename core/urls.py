from django.urls import path

from core import views

urlpatterns = [
    path('signup/', views.UserCreateView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
]
