from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from .models import Event
from django.views.decorators.csrf import csrf_exempt
import json
from .tasks import notify_event_created  # <-- import the task
@csrf_exempt
def event_list(request):
    if request.method == "GET":
        events = list(Event.objects.values())
        return JsonResponse(events, safe=False)
    
    elif request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    return HttpResponseNotAllowed(["GET", "OPTIONS"])


@csrf_exempt
def create_event(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            event = Event.objects.create(
                title=data["title"],
                description=data["description"],
                location=data["location"],
                start_time=data["start_time"],
                end_time=data["end_time"]
            )
            notify_event_created.delay(event.title, event.location)
            return JsonResponse({"message": "Event created", "event_id": event.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    elif request.method == "OPTIONS":
        response = HttpResponse()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    return HttpResponseNotAllowed(["POST", "OPTIONS"])

