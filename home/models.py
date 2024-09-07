from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=30)

  class Meta:
    verbose_name_plural = "categories"

  def __str__(self):
    return self.name
  

class Post(models.Model):
  title = models.CharField(max_length=255)
  body = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  created_by = models.CharField(max_length=255)
  last_modified = models.DateTimeField(auto_now=True)
  modified_by = models.CharField(max_length=255)
  categories = models.ManyToManyField('Category', related_name='posts')
  slug = models.SlugField(max_length=255, unique=True)

  def __str__(self):
    return self.title
  

class Comment(models.Model):
  author = models.CharField(max_length=255)
  body = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  post = models.ForeignKey('Post', on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.author} on {self.post}"