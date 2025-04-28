from django.db import models

class GalleryItem(models.Model):
    """Model for gallery items."""
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='gallery/')
    video = models.FileField(upload_to='videos/gallery/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']
        verbose_name = "Élément de galerie"
        verbose_name_plural = "Éléments de galerie"

class GalleryCollection(models.Model):
    """Model for grouping gallery items into collections."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']
        verbose_name = "Collection de galerie"
        verbose_name_plural = "Collections de galerie"

class GalleryCollectionItem(models.Model):
    """Model for grouping gallery items into collections."""
    collection = models.ForeignKey(GalleryCollection, on_delete=models.CASCADE, related_name='items')
    image = models.ImageField(upload_to='gallery/collections/')
    
    def __str__(self):
        return f"Image for {self.collection.title}"