from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from accounts.models import CustomUser

class Deck(models.Model):
    ARCANA_CHOICES = [
        ('Major', 'Major Arcana'),
        ('Minor', 'Minor Arcana'),
    ]
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    arcana_type = models.CharField(max_length=10, choices=ARCANA_CHOICES)
    description_upright = models.TextField()
    description_reversed = models.TextField()
    image = models.ImageField(upload_to='card_images/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.number} - {self.name}"
    
    
class Reading(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    card = models.ForeignKey(Deck, on_delete=models.CASCADE)
    is_reversed = models.BooleanField(default=False)
    date_drawn = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.card.name} ({self.date_drawn.strftime('%d/%m/%Y')})"
    