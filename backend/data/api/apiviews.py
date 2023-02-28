from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from typing import Sequence

from ..models import URLS
from .serializers import URLSSerilizer

class URLView(APIView):
    def get(self, request, format=None):
        return JsonResponse(
            {
                "message": "Welcome to data."
            }
        )
    def post(self, request, format=None):
        serializer = URLSSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    