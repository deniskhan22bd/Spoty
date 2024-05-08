from django.urls import path
from api.views import HealthCheckAPIView, RegistrationAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('health-check/', HealthCheckAPIView.as_view()),
    
    path('users/', RegistrationAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
