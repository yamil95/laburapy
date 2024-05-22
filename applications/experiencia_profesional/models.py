from django.db import models
from django.conf import settings

# Create your models here.
class Experiencia(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="experiencia_re", on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"

    def __str__(self):
        return self.name


class Photo(models.Model):
    album = models.ForeignKey(Experiencia, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='photos')
    caption = models.CharField(max_length=100, blank=True)



