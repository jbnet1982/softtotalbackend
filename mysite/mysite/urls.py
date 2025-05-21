from django.contrib import admin
from django.urls import path
from accounts.views import RegisterUserView, LoginView  # si lo estás usando directamente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterUserView.as_view(), name='register'),
    path('api/login/',   LoginView.as_view(),    name='token_obtain_pair'),
]