from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.http import HttpResponse

@api_view(['GET', 'POST'])
def register_user(request):
    if request.method == 'GET':
        return HttpResponse("This endpoint is for user registration. Please send a POST request.")
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

def home(request):
    return HttpResponse("Welcome to the Chat App!")
