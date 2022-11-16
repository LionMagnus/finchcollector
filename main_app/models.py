from django.db import models

# Create your models here.
class Finch(models.Model):
  BOOL_CHOICES = ((True, 'Male'), (False, 'Female'))
  name = models.CharField(max_length=100)
  gender = models.BooleanField(choices=BOOL_CHOICES)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  # Changing this instance method
  # does not impact the database, therefore
  # no makemigrations is necessary
  def __str__(self):
    return f'{self.name} ({self.id})'