from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from applications.users.models import User
# Create your models here.

class Review (models.Model):

    reseña = models.TextField(blank=True)
    
    estrellas = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    usuario = models.ForeignKey(User, verbose_name=("usuarios"), on_delete=models.CASCADE)
