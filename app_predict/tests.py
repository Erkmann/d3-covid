from django.conf.urls import url
from django.test import TestCase
from datetime import date, timedelta
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .utils import check_yesterday, get_yesterday
from .models import Dia


class UtilsTest(TestCase):
    def setUp(self):
        self.ontem = date.today() - timedelta(days=1)

    def test_get_yesterday(self):  # testa se esta retornando 'ontem'
        self.assertEqual(get_yesterday(), self.ontem)

    def test_check_yesterday(
        self,
    ):  # testa se checkar se ontem esta cadastrado esta funcionando
        self.assertEqual(check_yesterday(), False)

        Dia.objects.create(data=self.ontem, casos=1)
        self.assertEqual(check_yesterday(), True)


class PredictTest(APITestCase):
    def setUp(self):
        self.url = "/api/v1/predict/"

    def test_not_allowed(self):  # testa predict com <= 0 e com float/string
        response = self.client.get(self.url + "0/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.get(self.url + "-1/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(self.url + "1.2/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(self.url + "aa/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_success(self):  # testa predict com paremtro valido
        response = self.client.get(self.url + "4/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
