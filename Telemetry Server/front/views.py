from django.views.generic import ListView
from .models import Player, Telemetry

class TelemetryListView(ListView):
    model = Player
    template_name = 'telemetry_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        player_telemetries = {}
        for player in context['object_list']:
            telemetries = Telemetry.objects.filter(player=player).order_by('-datetime')
            player_telemetries[player] = telemetries
        context['player_telemetries'] = player_telemetries
        return context
