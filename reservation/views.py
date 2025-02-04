from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serialization import BookingSerializer, MenuSerializer
from rest_framework.permissions import IsAuthenticated

class BookingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items =  Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer)
    
class MenuView(APIView):
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer)

class SingleMenuItemView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        item = Menu.objects.get(pk=pk)
        serializer = MenuSerializer(item)
        return Response(serializer)
