from django.db import models

class AboutContent(models.Model):
    """Model for about page content."""
    title = models.CharField(max_length=255)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Contenu À propos"
        verbose_name_plural = "Contenus À propos"

class Founder(models.Model):
    """Model for foundation founders."""
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField(upload_to='founders/')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Fondateur"
        verbose_name_plural = "Fondateurs"

class Partner(models.Model):
    """Model for foundation partners."""
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='partners/')
    website = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Partenaire"
        verbose_name_plural = "Partenaires"