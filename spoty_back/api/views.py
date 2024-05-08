from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from api.serializers import RegistrationSerializer
# Create your views here.

class HealthCheckAPIView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)
    
    
class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

