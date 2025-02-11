from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response


class IndexView(generics.GenericAPIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})