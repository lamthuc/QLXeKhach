from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('customer', 'Customer'),
        ('driver', 'Driver'),
        ('employee', 'Employee'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='uploads/%Y/%m')


class Route(models.Model):
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    estimate_time = models.CharField(max_length=20)


class Coach(models.Model):
    number_plate = models.CharField(max_length=20, primary_key=True)
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null =True)
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField(null=True)
    is_holiday = models.BooleanField(default=False)

class Delivery(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_address = models.CharField(max_length=200)
    receiver_name = models.CharField(max_length=100)
    receiver_address = models.CharField(max_length=200)
    delivery_time = models.DateTimeField(null=True)

class SeatDetail(models.Model):
    STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('available', 'Available'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    seat_code = models.CharField(max_length=20, primary_key=True)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class BusCompany(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus_company = models.ForeignKey(BusCompany, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'bus_company')
class Ticket(models.Model):
    seat_detail = models.ForeignKey(SeatDetail, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)




