from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item
from .serializers import ItemSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def getData(request):
    name = request.GET.get('query', '')

    # If you want a single item:
    try:
        item = Item.objects.get(name=name)
        serializer = ItemSerializer(item, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response({'error': 'Item not found'}, status=404)


@api_view(['POST'])
def addItem(request):
    try:
        serializer = ItemSerializer(data=request.data)

        if serializer.is_valid():
            # Save the new item
            serializer.save()

            return Response({
                'message': 'Item created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            'error': 'Invalid data',
            'details': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)