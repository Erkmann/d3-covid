from django.shortcuts import render
from datetime import datetime, timedelta
import json

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import populate_total

from .models import Dia


class PredictView(APIView):
    def get(self, request, *args, **kwargs):
        populate_total()  # popula com os ultimos dados
        try:
            days = int(kwargs["days"])
            if days <= 0:  # verifica se o numero de dias eh <= 0
                return Response(
                    {"message": "Número nao pode ser <= 0"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            data_filtro = (
                datetime.today() - timedelta(days=days)
            ).date()  # define o filtro de acordo com n, de quantos dias vai usar como parametro para a predicao

            dias = Dia.objects.filter(data__gte=data_filtro)

            if not dias:
                dias = (
                    Dia.objects.all().order_by("-data").first()
                )  # se nao encontrar nenhum dia (nao foi encontrado 'ontem' no CSV pois nao foi atualizado na fonte ainda)

            casos = []

            for dia in dias:
                casos.append(dia.casos) # cria uma lista com os numeros para serem usados como parametro

            return Response(data=casos, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(data={e}, status=status.HTTP_400_BAD_REQUEST)
