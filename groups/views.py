from django.shortcuts import get_object_or_404, render, redirect
from django.http.response import HttpResponse
from django.http.request import HttpRequest

from groups.models import GroupModel


def groups_view(request: HttpRequest) -> HttpResponse:
    """
    Groups list view
    """
    groups = GroupModel.objects.all()
    return render(request, "groups/all_groups.html", {'groups': groups})
