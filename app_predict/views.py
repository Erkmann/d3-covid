from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import populate_total


class PredictView(APIView):
    def get(self, request, *args, **kwargs):
        populate_total()
        
        days = kwargs['days']

        return Response(data={}, status=status.HTTP_204_NO_CONTENT)
