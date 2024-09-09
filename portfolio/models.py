from django.db import models

# Create your models here.
class Portfolio(models.Model):
  class Meta:
    verbose_name_plural = "Portfolio Items"

  title = models.CharField(max_length=255)
  description = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  created_by = models.CharField(max_length=255)
  last_modified = models.DateTimeField(auto_now=True)
  modified_by = models.CharField(max_length=255)
  slug = models.SlugField(max_length=255, unique=True)
  cover_image = models.ImageField(upload_to='images/')

  def __str__(self):
    return self.title