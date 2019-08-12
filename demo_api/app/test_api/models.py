from django.db import models
from django.core.validators import MinValueValidator

from app.test_api.validators import *

# Create your models here.

class tabla(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    superficie = models.IntegerField(validators=[MinValueValidator(0), validate_number])
    email = models.EmailField(max_length=50)