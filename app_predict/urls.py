from django.urls import path

from .views import PredictView

app_name = 'predict'
urlpatterns = [
    path('predict/<int:days>/', PredictView.as_view(), name='predict')
]
