from django.http import HttpResponse
from django.http.response import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from game.utils import db_model, parse_json
from bson.objectid import ObjectId


def index(request):
    return HttpResponse("Hello, world. You're at the game index.")

@api_view(['GET'])
def champion_details(request, id):
    if request.method == "GET":
        try: 
            champion = db_model["champion"].find_one({"_id": ObjectId(id)})
            return JsonResponse(parse_json(champion), safe=False)
        except ValueError:
            print(ValueError)
            return JsonResponse({'message': 'The champion does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    

@api_view(['GET'])
def get_random_champion(request):
    if request.method == "GET":
        try: 
            random_champion = list(db_model["champion"].aggregate([{ "$sample": { "size": 1 } }]))[0]
            return JsonResponse(parse_json(random_champion), safe=False)
        except : 
            return JsonResponse({'message': 'The champion does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    