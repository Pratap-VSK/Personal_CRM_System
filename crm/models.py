from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Contact(models.Model):
    CATEGORY_CHOICES = [
        ('Friend', 'Friend'),
        ('Client', 'Client'),
        ('Mentor', 'Mentor'),
        ('Family', 'Family'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Client')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now, auto_now_add=False)

    def __str__(self):
        return self.name


class Interaction(models.Model):
    INTERACTION_TYPES = [
        ('Call', 'Call'),
        ('Meeting', 'Meeting'),
        ('Message', 'Message'),
    ]

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='interactions')
    date = models.DateField()
    interaction_type = models.CharField(max_length=50, choices=INTERACTION_TYPES)
    summary = models.TextField()

    def __str__(self):
        return f"{self.contact.name} - {self.date}"
