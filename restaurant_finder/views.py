from restaurant_finder.models import Restaurant
from restaurant_finder.serializers import RestaurantSerializer
from django.shortcuts import render
from rest_framework import generics

class ListCreateRestaurants(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def perform_create(self, serializer):
        address = serializer.initial_data['address']
        g = geocoder.google(address)
        latitude = latlang[0]
        longitude = latlang[1]
        pnt = 'POINT(' + str(longitude) + ' ' + str(latitude)+')'
        serializer.save(location=pnt)
        read_only_fields = ('location',)
