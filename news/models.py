from django.db import models
from django.utils import timezone

class Event(models.Model):
    """Model for upcoming events and weekly services."""
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='events/')
    is_upcoming = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title} - {self.date}"
    
    def save(self, *args, **kwargs):
        # Automatically set is_upcoming based on date
        if self.date < timezone.now().date():
            self.is_upcoming = False
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['date']
        verbose_name = "Événement"
        verbose_name_plural = "Événements"