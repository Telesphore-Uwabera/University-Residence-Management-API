from django.db import models
from django.contrib.auth.models import User
from encrypted_model_fields.fields import EncryptedCharField


class Building(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


class Room(models.Model):
    BUILDING_TYPES = [
        ('single', 'Single'),
        ('double', 'Double'),
    ]
    number = models.CharField(max_length=10)
    building = models.ForeignKey(Building, related_name='rooms', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=BUILDING_TYPES)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.number} - {self.building.name}'


class Resident(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='residents', on_delete=models.CASCADE)
    contact_number = EncryptedCharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.room.number}'


class MaintenanceRequest(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    issue = models.TextField()
    location = models.ForeignKey(Room, on_delete=models.CASCADE)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.issue} - {self.priority}'


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.ForeignKey(Building, related_name='events', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Communication(models.Model):
    resident = models.ForeignKey(Resident, related_name='communications', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Communication from {self.resident.user.username} on {self.created_at}'


class RegistrationForResident(models.Model):
    resident = models.ForeignKey(Resident, related_name='registrations', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='registrations', on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f'Registration for {self.resident.user.username} - {self.room.number}'


class Payment(models.Model):
    MONTHS = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]
    resident = models.ForeignKey(Resident, related_name='payments', on_delete=models.CASCADE)
    month = models.CharField(max_length=20, choices=MONTHS)
    year = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment from {self.resident.user.username} for {self.month} {self.year}'