from django.shortcuts import get_object_or_404, render, redirect
from django.http.response import HttpResponse
from django.http.request import HttpRequest

from users.models import UserModel


def users_view(request: HttpRequest) -> HttpResponse:
    """
    Homepage
    Users list view
    """
    users = UserModel.objects.all()
    return render(request, "users/all_users.html", {'users': users})
