from django.http import HttpResponse
from django.http.response import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from game.utils import db_model, parse_json, lookup_all_properties
from bson.objectid import ObjectId

# Should be saved in database later.
current_champion = {}


def index(request):
    return HttpResponse("Hello, world. You're at the game index.")


@api_view(['GET'])
def champion_details(request, id):
    if request.method == "GET":
        try:
            print([*lookup_all_properties])
            champion = list(db_model["champion"].aggregate(
                [*lookup_all_properties, {"$sample": {"size": 1}}]))
            print(len(champion))
            return JsonResponse(parse_json(champion[0]), safe=False)
        except ValueError:
            print(ValueError)
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
            champion_to_check = list(
                db_model["champion"].aggregate([*lookup_all_properties, {"$match": {"$and": [{"champion_id": to_check}]}}]))
        except ValueError:
            return JsonResponse({'message': 'The champion to be checked does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        try:
            champion_reference = list(
                db_model["champion"].aggregate([*lookup_all_properties, {"$match": {"$and": [{"_id": ObjectId(reference)}]}}]))
        except ValueError:
            return JsonResponse({'message': 'The champion was not generated correctly.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_random_champion(request):
    global current_champion
    if request.method == "GET":
        try:
            random_champion = list(db_model["champion"].aggregate([
                {"$sample": {"size": 1}},
            ]))[0]
            current_champion = random_champion
            # Return MongoDB generated id only (champion_id gives a rough idea of how
            # the chamion ranks in the alphabet and will be used for check_champion instead).
            return JsonResponse(parse_json(random_champion['_id']), safe=False)
        except ValueError:
            print(ValueError)
            return JsonResponse({'message': 'The champion does not exist'}, status=status.HTTP_404_NOT_FOUND)
