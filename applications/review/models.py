from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()
# Create your models here.

class Review (models.Model):

    reseña = models.TextField(blank=True)
    
    estrellas = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="review", on_delete=models.CASCADE)
