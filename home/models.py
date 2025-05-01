from django.db import models
from django.utils import timezone
from datetime import timedelta

class WeeklyService(models.Model):
    """Model for weekly services displayed on the homepage."""
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255, help_text="e.g. Lausanne, Suisse")
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    
    def __str__(self):
        return f"{self.title} - {self.date}"
    
    class Meta:
        ordering = ['-date']
        verbose_name = "Service de la semaine"
        verbose_name_plural = "Services de la semaine"

class HomePageSection(models.Model):
    """Configurable sections for the homepage."""
    SECTION_TYPES = (
        ('cultes', 'Cultes'),
        ('evenements', 'Événements'),
        ('theologie', 'Cours de Théologie'),
    )
    
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES)
    title = models.CharField(max_length=255)
    display_order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['display_order']
        verbose_name = "Section de la page d'accueil"
        verbose_name_plural = "Sections de la page d'accueil"

class SpecialEvent(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    time = models.TimeField()
    theme = models.CharField(max_length=255)
    expire_after_days = models.PositiveIntegerField(default=7)
    est_culte_de_la_semaine = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.est_culte_de_la_semaine:
            # Unset this flag for all other SpecialEvent instances
            SpecialEvent.objects.filter(est_culte_de_la_semaine=True).update(est_culte_de_la_semaine=False)
            self.est_culte_de_la_semaine = True
        super().save(*args, **kwargs)

    def is_active(self):
        return timezone.now() < self.created_at + timedelta(days=self.expire_after_days)

    def __str__(self):
        return f"{self.title} - {self.date}"

    class Meta:
        ordering = ['-created_at']

class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    is_song = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Culte(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    description_main = models.TextField()
    description_secondary = models.TextField(blank=True, null=True)
    miniature = models.ImageField(upload_to='culte_thumbnails/')
    is_song = models.BooleanField(default=False)  # for videos
    videos = models.ManyToManyField(Video, blank=True)

    def __str__(self):
        return f"Culte du {self.date}"
