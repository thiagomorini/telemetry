from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=50)
    session_id = models.CharField(max_length=36, null=True, blank=True)

    def __str__(self):
        return self.username

class Telemetry(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    position_x = models.FloatField()
    position_y = models.FloatField()
    position_z = models.FloatField()
    keys_pressed = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.player.username} ({self.datetime})'
