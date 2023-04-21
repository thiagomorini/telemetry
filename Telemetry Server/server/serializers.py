from rest_framework import serializers
from .models import Player, Telemetry
from uuid import uuid4

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'username', 'session_id')

    def create(self, validated_data):
        session_id = validated_data.get('session_id', None)
        if not session_id:
            validated_data['session_id'] = str(uuid4())
        return super().create(validated_data)   

class TelemetrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Telemetry
        fields = ('id', 'player', 'datetime', 'position_x', 'position_y', 'position_z', 'keys_pressed')
