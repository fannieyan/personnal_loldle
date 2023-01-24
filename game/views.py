from pymongo import MongoClient
from django.http import HttpResponse
from django.http.response import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from game.serializers import ChampionSerializer
from game.utils import db_model


def index(request):
    return HttpResponse("Hello, world. You're at the game index.")

@api_view(['GET'])
def champion_details(request, champion_id):
    if request.method == "GET":
        try: 
            champion = db_model["champion"].find_one({"champion_id": int(champion_id)})
            ## TODO : Serialize id for better performance when getting champion to check properties
            ## And join with different collections
            champion_serializer = ChampionSerializer(champion, many=False)
            return JsonResponse(champion_serializer.data, safe=False)
        except: 
            return JsonResponse({'message': 'The champion does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    

@api_view(['GET'])
def random_champion(request):
    if request.method == "GET":
        try: 
            random_champ = list(db_model["champion"].aggregate([{ "$sample": { "size": 1 } }]))[0]
            champion_serializer = ChampionSerializer(random_champ, many=False)
            print(champion_serializer.data)
            return JsonResponse(champion_serializer.data, safe=False)
        except : 
            return JsonResponse({'message': 'The champion does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    