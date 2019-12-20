from django.db import models

# Create your models here.
class Categoria(models.Model):
	nombre = models.CharField(max_length=200)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre	
	