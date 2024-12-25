from django.shortcuts import render
from django.http import JsonResponse
from decouple import config
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group

from .serializers import AttendeeSerializer
from .models import Attendee
from .forms import AttendeeForm

# For Admin
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def login(request):
    pass

def logout(request):
    pass

def data(request):
    pass

def create_attendee(request):
    pass

def update_attendee(request, pk):
    pass

def delete_attendee(request, pk):
    pass

# For User
def post_data(request):
    pass


