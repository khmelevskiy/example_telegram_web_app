import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import ClickHistory, User


def index(request):
    return render(request, "index.html")


@csrf_exempt
def click_coin(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        telegram_id = data.get("telegram_id")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        is_premium = data.get("is_premium", False)
        user_data = data.get("user_data", {})  # Get user data
        init_data = data.get("init_data", {})  # Get initialization data

        user, created = User.objects.get_or_create(telegram_id=telegram_id)
        if created:
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.is_premium = is_premium
            user.user_data = json.dumps(user_data)  # Convert to JSON string
            user.init_data = json.dumps(init_data)  # Convert to JSON string
        else:
            # Update data if user already exists
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.is_premium = is_premium
            user.user_data = json.dumps(user_data)
            user.init_data = json.dumps(init_data)

        user.points += 1
        user.save()

        # Save click history
        ClickHistory.objects.create(user=user, points_after_click=user.points)

        return JsonResponse({"points": user.points})

    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def get_points(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        telegram_id = data.get("telegram_id")

        try:
            user = User.objects.get(telegram_id=telegram_id)
            return JsonResponse({"points": user.points})
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

    return JsonResponse({"error": "Invalid request method"}, status=405)
