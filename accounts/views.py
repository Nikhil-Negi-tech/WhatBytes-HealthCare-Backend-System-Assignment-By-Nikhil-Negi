from rest_framework import generics
from .serializers import RegisterSerializer
# RegisterView will handle user registration at /api/auth/register/ endpoint
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer