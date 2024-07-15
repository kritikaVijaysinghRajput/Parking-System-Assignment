from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Custom related name to avoid clash
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Custom related name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )


class Vehicle(models.Model):
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.license_plate})"

class ParkingSession(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(auto_now_add=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Session for {self.vehicle.license_plate}"
