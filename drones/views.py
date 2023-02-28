from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import DroneCategorySerializer, DroneSerializer, PilotCompetitionSerializer, PilotSerializer
from .models import DroneCategory, Drone, Competition, Pilot

# Create your views here.

# DroneCategory Views

class DroneCategoryList(ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-list'

class DroneCategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name= 'dronecategory-detail'


# Drone Views

class DroneList(ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-list'

class DroneDetail(RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'


# Pilot Serializer
class PilotList(ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = "pilot-list"

class PilotDetail(RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = "pilot-detail"


# PilotCompetition Serializer
class CompetitionList(ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = "competition-list"

class CompetitonDetail(RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = "competition-detail"

