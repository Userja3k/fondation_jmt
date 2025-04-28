from django.db import models

class TheologyCourse(models.Model):
    """Model for theology courses."""
    COURSE_TYPES = (
        ('online', 'Cours en ligne'),
        ('inperson', 'Cours en présentiel'),
        ('conference', 'Conférence'),
        ('seminar', 'Séminaire'),
    )
    
    title = models.CharField(max_length=255)
    date = models.DateField()
    course_type = models.CharField(max_length=20, choices=COURSE_TYPES)
    description = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True, help_text="Required for in-person courses")
    image = models.ImageField(upload_to='theology/')
    video_url = models.URLField(blank=True, null=True, help_text="YouTube or video URL")
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']
        verbose_name = "Cours de théologie"
        verbose_name_plural = "Cours de théologie"