from rest_framework import serializers
from game.models import ChampionProperties


def serializeStringArray(string):
    stringWithoutBrackets = string[1:-1]
    return stringWithoutBrackets.split(',')


class ChampionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChampionProperties
        fields = '__all__'

    # PostgreSQL arrays are retrieved as strings. This is a workaround.
    lanes = serializers.SerializerMethodField(read_only=True)
    species = serializers.SerializerMethodField(read_only=True)
    ranges = serializers.SerializerMethodField(read_only=True)
    regions = serializers.SerializerMethodField(read_only=True)

    def get_lanes(self, obj):
        return serializeStringArray(obj.lanes)

    def get_species(self, obj):
        return serializeStringArray(obj.species)

    def get_ranges(self, obj):
        return serializeStringArray(obj.ranges)

    def get_regions(self, obj):
        return serializeStringArray(obj.regions)
