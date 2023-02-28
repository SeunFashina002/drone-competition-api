from django.urls import path

from drones.views import (
    DroneCategoryList, 
    DroneCategoryDetail, 
    DroneList, 
    DroneDetail,
    CompetitionList,
    CompetitonDetail,
    PilotList,
    PilotDetail,
)

urlpatterns = [
    path('api/v1/drone-category/', DroneCategoryList.as_view(), name=DroneCategoryList.name),
    path('api/v1/drone-category/<int:pk>/', DroneCategoryDetail.as_view(), name=DroneCategoryDetail.name),
    path('api/v1/drone/', DroneList.as_view(), name=DroneList.name),
    path('api/v1/drone/<int:pk>', DroneDetail.as_view(), name=DroneDetail.name),
    path('api/v1/competition/', CompetitionList.as_view(), name=CompetitionList.name),
    path('api/v1/competion/<int:pk>', CompetitonDetail.as_view(), name=CompetitonDetail.name),
    path('api/v1/pilot/', PilotList.as_view(), name=PilotList.name),
    path('api/v1/pilot/<int:pk>', PilotDetail.as_view(), name=PilotDetail.name),


]