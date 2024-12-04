from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Item
from .serializers import ItemSerializer
from rest_framework import status
# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate


@api_view(['GET'])
def getData(request):
    """Get items by name"""
    name = request.GET.get('query', '')
    try:
        if name:
            items = Item.objects.filter(name__icontains=name)
        else:
            items = Item.objects.all()

        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def addItem(request):
    """
    Add a new item to the database
    """
    print("Received data:", request.data)  # Debug print

    try:
        # Create item instance
        serializer = ItemSerializer(data={
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'amount_available': request.data.get('amount_available'),
            'img_url': request.data.get('img_url')
        })

        print("Serializer data:", serializer.initial_data)  # Debug print

        if serializer.is_valid():
            item = serializer.save()
            print("Saved item:", {  # Debug print
                'name': item.name,
                'description': item.description,
                'amount_available': item.amount_available,
                'img_url': item.img_url
            })
            return Response({
                'message': 'Item created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            print("Serializer errors:", serializer.errors)  # Debug print
            return Response({
                'error': 'Invalid data',
                'details': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print(f"Error creating item: {str(e)}")  # Debug print
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def login_view(request):
    """Handle login and return JWT token"""
    try:
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Login successful',
                'token': str(refresh.access_token)
            })
        else:
            return Response({
                'error': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_auth(request):
    """Check if user is authenticated and is admin"""
    if request.user.is_staff:
        return Response({
            'is_authenticated': True,
            'is_admin': True,
            'username': request.user.username
        })
    return Response({
        'is_authenticated': True,
        'is_admin': False,
        'username': request.user.username
    })
