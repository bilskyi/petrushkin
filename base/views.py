from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from base.models import Album, Picture, Tag
from base.serializers import AlbumSerializer, PictureSerializer, TagSerializer


class IndexView(generics.GenericAPIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})
    

class AlbumViewSet(ModelViewSet):
    model = Album
    serializer_class = AlbumSerializer


class PictureViewSet(ModelViewSet):
    model = Picture
    serializer_class = PictureSerializer
