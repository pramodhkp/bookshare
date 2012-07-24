from userprofile.models import User 
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext


def profile(request):
    return render(request, 'user.html')