from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Reloj(models.Model):
    """
    Model representing watch
    """
    nombre = models.CharField(max_length=100, help_text="Introducir nombre representativo del reloj")
    marca = models.CharField(max_length=20, help_text="Introducir marca del reloj")
    descipcion = models.CharField(max_length=400, help_text="Introducir descripcion [opcional]",blank=True)
    precio = models.FloatField(max_length=10, help_text="Introducir precio del reloj")
    imagen = models.ImageField(upload_to='productos',default='productos/default.jpg', help_text="Introducir imagen del producto[opcional]")
    def get_absolute_url(self):
        """
        Returns the url to access a particular watch instance
        """
        return reverse('watch-detail',args=[str(self.id)])
    def __str__(self):
        """
        Returns string representation of the Model object. (equivalent to "toString" function)
        """
        return self.nombre

class Anillo(models.Model):
    """
    Model representing rings
    """
    nombre = models.CharField(max_length=100, help_text="Introducir nombre representativo del anillo")
    descripcion = models.CharField(max_length=400, help_text="Introducir descripcion [opcional]",blank=True)
    precio = models.FloatField(max_length=10, help_text="Introducir precio del anillo")
    diametro = models.IntegerField(help_text="Introducir diametro del anillo")
    def get_absolute_url(self):
        """
        Returns the url to access a particular ring instance
        """
        return reverse('ring-detail',args=[str(self.id)])
    def __str__(self):
        """
        Returns string representation of the Model object. (equivalent to "toString" function)
        """
        return self.nombre

class Cadena(models.Model):
    """
    Model representing chains
    """
    nombre = models.CharField(max_length=100, help_text="Introducir nombre representativo de la cadena")
    descripcion = models.CharField(max_length=400, help_text="Introducir descripcion [opcional]",blank=True)
    precio = models.FloatField(max_length=10, help_text="Introducir precio del cadena")
    def get_absolute_url(self):
        """
        Returns the url to access a particular chain instance
        """
        return reverse('chain-detail',args=[str(self.id)])
    def __str__(self):
        """
        Returns string representation of the Model object. (equivalent to "toString" function)
        """
        return self.nombre
class Pendiente(models.Model):
    """
    Model representing earrings
    """
    nombre = models.CharField(max_length=100, help_text="Introducir nombre representativo del pendiente")
    descripcion = models.CharField(max_length=400, help_text="Introducir descripcion [opcional]",blank=True)
    precio = models.FloatField(max_length=10, help_text="Introducir precio del pendiente")
    def get_absolute_url(self):
        """
        Returns the url to access a particular earring instance
        """
        return reverse('earring-detail',args=[str(self.id)])
    def __str__(self):
        """
        Returns string representation of the Model object. (equivalent to "toString" function)
        """
        return self.nombre

class Compra(models.Model):
    """
    Model representing purchases
    """
    fecha = models.DateField(blank=True,help_text="Introducir fecha en la que se realizo la compra",null=True)
    producto = models.IntegerField(help_text="Introducir id del producto (reloj,cadena ect..)")
    status = (
        ('r', 'Reloj'),
        ('c', 'Cadena'),
        ('a', 'Anillo'),
    )
    tipo_producto = models.CharField(max_length=1, choices=status, default='r', help_text='Tipo producto')
    def get_absolute_url(self):
        """
        Returns the url to access a particular chain instance
        """
        return reverse('purchase-detail',args=[str(self.id)])
    def __str__(self):
        """
        Returns string representation of the Model object. (equivalent to "toString" function)
        """
        return self.tipo_producto
