from rest_framework import serializers 
from game.models import champion
 
 
class ChampionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = champion
        fields = ('id',
                  'champion_id',
                  'champion_name')
