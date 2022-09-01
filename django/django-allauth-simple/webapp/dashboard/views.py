from django.shortcuts import render, redirect
import json
from allauth.account.decorators import login_required

def home(request):
    """
    Everyone Can Open This Basic View
    """
    user = request.user
    if str(user) == "AnonymousUser":
        user = ""
    return render(request, 'dashboard/home.html', {"username":user})

@login_required
def private_data(request):
    """
    This view is protected and can only be viewed by logged in users
    """
    user = request.user
    return render(request, 'dashboard/private_data.html', {"username":user})