from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import MyUser
from .serializers import MyUserSerializer


class RegisterUser(APIView):
    def post(self, request):
        serializer = MyUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'email': serializer.data['email'],
                'id': repr(MyUser.objects.get(email=serializer.data['email']).id),
            }
            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
