from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class GalleryItem(models.Model):
    """Model for gallery items."""
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='gallery/')
    video = models.FileField(upload_to='videos/gallery/', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            img = img.convert('RGB')
            img = img.resize((800, 600))
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            new_name = f"{self.image.name.rsplit('.', 1)[0]}.webp"
            self.image.save(new_name, ContentFile(img_io.getvalue()), save=False)
        super().save(*args, **kwargs)
    
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
    
    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            img = img.convert('RGB')
            img = img.resize((800, 600))
            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)
            new_name = f"{self.image.name.rsplit('.', 1)[0]}.webp"
            self.image.save(new_name, ContentFile(img_io.getvalue()), save=False)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Image for {self.collection.title}"
