from django.db import models

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