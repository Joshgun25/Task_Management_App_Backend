from django.urls import path
from .views import RegisterView, LoginView, CustomLogout
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', CustomLogout.as_view(), name='logout'),
]

