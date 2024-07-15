from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Vehicle, ParkingSession

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'manufacturer', 'model', 'license_plate']

class ParkingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSession
        fields = ['id', 'vehicle', 'check_in_time', 'check_out_time', 'total_amount']
class ActiveVehicleSerializer(serializers.ModelSerializer):
    check_in_time = serializers.SerializerMethodField()

    class Meta:
        model = Vehicle
        fields = ['id', 'manufacturer', 'model', 'license_plate', 'check_in_time']

    def get_check_in_time(self, obj):
        active_session = ParkingSession.objects.filter(vehicle=obj, check_out_time__isnull=True).latest('check_in_time')
        return active_session.check_in_time