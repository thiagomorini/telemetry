from django.urls import path
from .views import (
    PlayerCreateAPIView,
    PlayerDetailAPIView,
    PlayerListAPIView,
    TelemetryCreateAPIView,
    TelemetryListPlayerAPIView,
    TelemetryListAPIView
)

urlpatterns = [
    path('players/', PlayerListAPIView.as_view(), name='player_list'),
    path('players/create/', PlayerCreateAPIView.as_view(), name='player_create'),  
    path('players/<str:session_id>/', PlayerDetailAPIView.as_view(), name='player_detail'),

    path('telemetry/', TelemetryListAPIView.as_view(), name='telemetry_list'),
    path('telemetry/create/', TelemetryCreateAPIView.as_view(), name='telemetry_create'),       
    path('telemetry/player/<int:player>/', TelemetryListPlayerAPIView.as_view(), name='telemetry_list_player'), 
]
