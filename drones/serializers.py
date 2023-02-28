from rest_framework import serializers
from .models import DroneCategory, Drone, Competition, Pilot
# from .views import 



class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    drones = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='drone-detail')
    class Meta:
        model = DroneCategory
        fields = (
            'url',
            'pk',
            'name',
            'drones',
        )

# url --> resolved the url using the view-name in the Drone Category view with denoted as 'name' keyword in views.py file

"""
(drones) itself is not present in our DroneCategory Model
but we know there is a many to one relationship between DroneCategory and Drone, meaning they are related

so to get the related drones for a particular drone category we uses HyperlinkedRelatedField
since we are dealing with links(urls) view_name = (drone-detail) helps to get the url associated to those drone instance
"""

class DroneSerializer(serializers.HyperlinkedModelSerializer):
    drone_category = serializers.SlugRelatedField(queryset= DroneCategory.objects.all(), slug_field='name')
    
    class Meta:
        model = Drone
        fields = (
            'url',
            'name',
            'drone_category',
            'manufacturing_date',
            'has_it_competed',
            'inserted_timestamp'
        )

"""
drone_category serves the same function as --> drone.drone_category.name (as related in the model)
where drone is the object of Drone model
drone_category is the foreignKey in the Drone model.

so unlike the HyperlinkedRelatedField, SlugRelatedField along with the slug_field variable allows us to return the name
of the related field, which is drone category in this case. Instead of the url

The DroneCategory field defines a name variable, so we specify it in the slug_field as our arguement
"""

class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    drone = DroneSerializer()
    
    class Meta:
        model = Competition
        fields = (
            'url',
            'pk',
            'distance_in_feet',
            'distance_achievement_date',
            'drone',
        )

class PilotSerializer(serializers.HyperlinkedModelSerializer):
    
    competitions = CompetitionSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(Pilot.GENDER_CHOICES)
    gender_description = serializers.CharField(source ='get_gender', read_only=True)

    class Meta:
        model = Pilot
        fields = (
            'url',
            'name',
            'gender', 
            'gender_description', 
            'races_count',
            'inserted_timestamp',
            'competitions',
        )


class PilotCompetitionSerializer(serializers.ModelSerializer):
    # Display the pilot's name
    pilot = serializers.SlugRelatedField(queryset=Pilot.objects.all(), slug_field='name')
    # Display the drone's name
    drone = serializers.SlugRelatedField(queryset=Drone.objects.all(), slug_field='name')

    class Meta:
        model = Competition
        fields = (
        'url',
        'pk',
        'distance_in_feet',
        'distance_achievement_date',
        'pilot',
        'drone')
