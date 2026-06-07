from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView, ListAPIView, RetrieveUpdateDestroyAPIView, MyProfileAPIView

urlpatterns = [
    path('register/', RegisterView.as_view()),

    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('profile/', ListAPIView.as_view()),
    path('profile/<int:pk>/', RetrieveUpdateDestroyAPIView.as_view()),

    path('my-profile/', MyProfileAPIView.as_view()),
]