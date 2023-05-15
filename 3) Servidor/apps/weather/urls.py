from django.urls import path
from .views import ListDHT11SensorData,AddDHT11SensorData,ToggleLEDView


urlpatterns =[
    path('list', ListDHT11SensorData.as_view()),
    path('add', AddDHT11SensorData.as_view()),
    path('toggle_led', ToggleLEDView.as_view()),
]