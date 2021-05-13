from django.contrib import admin
from django.urls import path, include

from app_predict import urls as app_predict

urlpatterns = [
    path('api/v1/', include(app_predict)),
]
