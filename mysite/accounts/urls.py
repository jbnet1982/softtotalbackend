# mysite/urls.py
from django.urls import path, include
from accounts.views import RegisterView, LoginView, ChangePasswordView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/',   LoginView.as_view(),    name='token_obtain_pair'),
    path('api/password/',ChangePasswordView.as_view(), name='change_password'),
]