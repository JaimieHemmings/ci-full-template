from django.db import models

# Create your models here.
class Project(models.Model):

  PROJECT_STATUS_CHOICES = (
      ('awaiting_customer', 'Awaiting Customer'),
      ('in_progress', 'In Progress'),
      ('on_hold', 'On Hold'),
      ('completed', 'Completed'),
      ('cancelled', 'Cancelled'),
  )

  title = models.CharField(max_length=255)
  description = models.TextField()
  image = models.ImageField(upload_to='images/', blank=True, null=True)
  created_on = models.DateTimeField(auto_now_add=True)
  github_link = models.URLField(max_length=255, default=None, blank=True, null=True)
  live_link = models.URLField(max_length=255, default=None, blank=True, null=True)
  price_quoted = models.DecimalField(max_digits=10, decimal_places=2)
  deposit_amount = models.DecimalField(max_digits=10, decimal_places=2)
  deposit_paid = models.BooleanField(default=False)
  completed = models.BooleanField(default=False)
  project_status = models.CharField(max_length=100, choices=PROJECT_STATUS_CHOICES)
  final_amount_due = models.DecimalField(max_digits=10, decimal_places=2)
  final_amount_paid = models.BooleanField(default=False)
  owner = models.CharField(max_length=255)

  def __str__(self):
    return self.title