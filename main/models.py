from django.db import models

# Create your models here.



class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre 

class Subcategoria(models.Model):
    nombre = models.CharField(max_length=200)
    estado = models.BooleanField(default=True)
    categoria = models.ManyToManyField(Categoria)
    #categoria = models.ForeignKey(Categoria, null=True,default=1,on_delete = models.CASCADE) # 

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    subcategoria = models.ForeignKey(Subcategoria,default=1,on_delete= models.CASCADE) #,unique=True
    categoria = models.ForeignKey(Categoria,blank=True, default=1,on_delete = models.CASCADE) #

    def __str__(self):
        return self.nombre

"""
class Producto(models.Model):
	nombre = models.CharField(max_length=200)


	def __str__(self):
		return self.nombre


class Subcategoria(models.Model):
	nombre = models.CharField(max_length=200)
	estado = models.BooleanField(default=True)
	producto = models.ManyToManyField(Producto) # unique=True,

	def __str__(self):
		return self.nombre


class Categoria(models.Model):
	nombre = models.CharField(max_length=200)
	estado = models.BooleanField(default=True)
	producto = models.ManyToManyField(Producto)
	subcategoria = models.ManyToManyField(Subcategoria)#, blank=True, default=None


	def __str__(self):
		return self.nombre
		
"""






"""class Producto(models.Model):
    nombre = models.CharField(max_length=128)

class Subcategoria(models.Model):
    nombre = models.CharField(max_length=128)
    producto = models.ManyToManyField(
        Producto,
        through='Categoria',
        through_fields=('subcategoria', 'producto'),
    )

class Categoria(models.Model):
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
"""


"""
class Categoria(models.Model):
	nombre = models.CharField(max_length=200)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre
		
class Subcategoria(models.Model):
	nombre = models.CharField(max_length=200)
	estado = models.BooleanField(default=True)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) # unique=True,

	def __str__(self):
		return self.nombre

class Producto(models.Model):
	nombre = models.CharField(max_length=200)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	subcategoria = models.ForeignKey(Subcategoria, on_delete= models.CASCADE)

	def __str__(self):
		return self.nombre	"""
	