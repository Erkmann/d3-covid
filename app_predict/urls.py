from django.urls import path

from .views import PredictView

urlpatterns = [
    path('predict/<int:days>/', PredictView.as_view(), name='predict')
]
