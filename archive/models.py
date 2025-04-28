from django.db import models

class ArchivedService(models.Model):
    """Model for archived services."""
    title = models.CharField(max_length=255)
    date = models.DateField()
    theme = models.CharField(max_length=255)
    description = models.TextField()
    verses = models.TextField(help_text="Enter Bible verses separated by commas")
    song_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='archives/')
    sermon_video = models.FileField(upload_to='videos/sermons/')
    song_video = models.FileField(upload_to='videos/songs/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.date}"
    
    class Meta:
        ordering = ['-date']
        verbose_name = "Service archivé"
        verbose_name_plural = "Services archivés"

class Debate(models.Model):
    """Model for student debates."""
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='debates/')
    video = models.FileField(upload_to='videos/debates/')
    
    def __str__(self):
        return f"{self.title} - {self.date}"
    
    class Meta:
        ordering = ['-date']
        verbose_name = "Débat"
        verbose_name_plural = "Débats"