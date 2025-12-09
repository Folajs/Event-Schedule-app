from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = authenticate(
            request,
            username=data.get("username"),
            password=data.get("password")
        )
        if user:
            login(request, user)
            return JsonResponse({"message": "Login successful"})
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=400)

@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({"message": "Logged out"})

@csrf_exempt
def register_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        from django.contrib.auth.models import User
        if User.objects.filter(username=data["username"]).exists():
            return JsonResponse({"error": "Username already exists"}, status=400)
        user = User.objects.create_user(
            username=data["username"],
            password=data["password"]
        )
        return JsonResponse({"message": "User created"})