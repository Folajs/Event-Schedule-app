from django.http import JsonResponse
from .models import RSVP
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def rsvp_list(request):
    if request.method == "GET":
        rsvps = list(RSVP.objects.values())
        return JsonResponse(rsvps, safe=False)

@csrf_exempt
def create_rsvp(request):
    if request.method == "POST":
        data = json.loads(request.body)
        RSVP.objects.create(
            event_id=data["event_id"],
            name=data["name"],
            email=data["email"],
            response=data["response"]
        )
        return JsonResponse({"message": "RSVP saved"})