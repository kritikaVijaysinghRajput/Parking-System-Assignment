from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import Vehicle, ParkingSession
from .serializers import UserSerializer, VehicleSerializer, ParkingSessionSerializer,ActiveVehicleSerializer
from django.utils import timezone

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class CheckInView(APIView):
    def post(self, request, *args, **kwargs):
        license_plate = request.data.get('license_plate')
        vehicle, created = Vehicle.objects.get_or_create(license_plate=license_plate, defaults=request.data)
        if not created:
            return Response({"message": "Vehicle already exists"}, status=status.HTTP_400_BAD_REQUEST)
        session = ParkingSession.objects.create(vehicle=vehicle)
        session_data = ParkingSessionSerializer(session).data
        return Response({"message": "Check-in successful", "data": session_data}, status=status.HTTP_200_OK)
class CheckOutView(APIView):
    def post(self, request, *args, **kwargs):
        license_plate = request.data.get('license_plate')
        try:
            vehicle = Vehicle.objects.get(license_plate=license_plate)
            session = ParkingSession.objects.filter(vehicle=vehicle, check_out_time__isnull=True).latest('check_in_time')
            session.check_out_time = timezone.now()
            duration = (session.check_out_time - session.check_in_time).total_seconds() / 3600
            session.total_amount = duration * 100
            session.save()
            return Response({"message": "Check-out successful", "total_amount": session.total_amount}, status=status.HTTP_200_OK)
        except Vehicle.DoesNotExist:
            return Response({"message": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)
        except ParkingSession.DoesNotExist:
            return Response({"message": "No active session found"}, status=status.HTTP_404_NOT_FOUND)

class ActiveVehiclesView(generics.ListAPIView):
    serializer_class = ActiveVehicleSerializer

    def get_queryset(self):
        return Vehicle.objects.filter(parkingsession__check_out_time__isnull=True).distinct()
class ActiveVehicleDetailView(APIView):
    def get(self, request, vehicle_id, *args, **kwargs):
        try:
            vehicle = Vehicle.objects.get(id=vehicle_id, parkingsession__check_out_time__isnull=True)
            vehicle_data = ActiveVehicleSerializer(vehicle).data
            return Response(vehicle_data, status=status.HTTP_200_OK)
        except Vehicle.DoesNotExist:
            return Response({"message": "Active vehicle not found"}, status=status.HTTP_404_NOT_FOUND)