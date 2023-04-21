from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Player, Telemetry
from .serializers import PlayerSerializer, TelemetrySerializer
from rest_framework.response import Response
from rest_framework import status

class PlayerListAPIView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetailAPIView(RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'session_id'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PlayerCreateAPIView(CreateAPIView):
    serializer_class = PlayerSerializer

class TelemetryListAPIView(ListAPIView):
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer

class TelemetryListPlayerAPIView(ListAPIView):
    serializer_class = TelemetrySerializer

    def get_queryset(self):
        player = self.kwargs.get('player')
        return Telemetry.objects.filter(player=player)

class TelemetryCreateAPIView(CreateAPIView):
    serializer_class = TelemetrySerializer
