from django.http import HttpResponse
from django.http.response import JsonResponse
import random
import os

from rest_framework import status
from rest_framework.decorators import api_view
from game.utils import check_properties
from game.models import ChampionProperties
from game.serializers import ChampionSerializer
from cryptography.fernet import Fernet

fernet = Fernet(os.getenv("FERNET_KEY").encode())


def index(request):
    return HttpResponse("Hello, world. You're at the game index.")


@api_view(['GET'])
def champion_details(request, id):
    if request.method == "GET":
        try:
            champion = ChampionProperties.objects.get(pk=id)
            champion_serializer = ChampionSerializer(champion)
            return JsonResponse(champion_serializer.data, safe=False)
        except ValueError:
            return JsonResponse({'message': 'The champion does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def check_champion(request):
    if request.method == "GET":
        # The _id of the reference champion.
        reference = request.query_params.get("ref")
        # The champion_id of the champion to be checked.
        to_check = request.query_params.get("champion")
        if (not (reference and to_check)):
            return JsonResponse({"message": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            decoded_champion = fernet.decrypt(reference.encode()).decode()
            champion_reference = ChampionSerializer(ChampionProperties.objects.get(
                pk=decoded_champion))
        except ValueError:
            return JsonResponse({'message': 'The reference champion does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            champion_to_check = ChampionSerializer(
                ChampionProperties.objects.get(pk=to_check))
        except ValueError:
            return JsonResponse({'message': 'The champion to check does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        result = check_properties(
            champion_reference.data, champion_to_check.data)
        return JsonResponse(result, safe=False)


@api_view(['GET'])
def get_random_champion(request):
    if request.method == "GET":
        try:
            champions = ChampionProperties.objects.all()
            random_index = random.randrange(0, len(champions))
            random_champion = champions[random_index]
            champion_serializer = ChampionSerializer(random_champion)
            encrypted_champion = fernet.encrypt(
                champion_serializer.data["champion"].encode())
            return JsonResponse(encrypted_champion.decode(), safe=False)
        except ValueError:
            return JsonResponse({'message': 'The champion does not exist'}, status=status.HTTP_404_NOT_FOUND)
