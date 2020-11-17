from django.db import models 
 
 
class Comprador(models.Model):
    #Choices
    COMUNAS = (
        ('CE','Cerrillos'),
        ('CN','Cerro Navia'),
        ('CO','Conchalí'),
        ('EB','El Bosque'),
        ('EC','Estación Central'),
        ('HU','Huechuraba'),
        ('IN','Independencia'),
        ('LA','La Cisterna'),
        ('LF','La Florida'),
        ('LG','La Granja'),
        ('LP','La Pintana'),
        ('LR','La Reina'),
        ('LC','Las Condes'),
        ('LB','Lo Barnechea'),
        ('LE','Lo Espejo'),
        ('LP','Lo Prado'),
        ('MA','Macul'),
        ('MP','Maipú'),
        ('ÑU','Ñuñoa'),
        ('PH','Padre Hurtado'),
        ('PAC','Pedro Aguirre Cerda'),
        ('PE','Peñalolén'),
        ('PI','Pirque'),
        ('PR','Providencia'),
        ('PU','Pudahuel'),
        ('PA','Puente Alto'),
        ('QU','Quilicura'),
        ('QN','Quinta Normal'),
        ('REC','Recoleta'),
        ('REN','Renca'),
        ('SB','San Bernardo'),
        ('SJ','San Joaquín'),
        ('SJM','San José de Maipo'),
        ('SM','San Miguel'),
        ('SR','San Ramón'),
        ('SAN','Santiago'),
    )
        
        
    #Atributos
    id_comprador = models.AutoField(primary_key=True)
    nombre_comprador = models.CharField(max_length=15)
    apellido_comprador = models.CharField(max_length=15)
    fono_comprador = models.CharField(max_length=12)
    dir_comprador = models.CharField(max_length=30)
    comuna_comprador = models.CharField(max_length=3, choices=COMUNAS)
    email_comprador = models.EmailField(max_length=25)
    usuario_comprador = models.CharField(max_length=15)
    pass_comprador = models.CharField(max_length=20)
 

    #Métodos
    def __str__(self): 
         return self.nombre_comprador
    def tostring(self):
         cadena=self.id_comprador+" "+self.apellido_comprador+" "+self.nombre_comprador+" "+self.fono_comprador+" "+self.dir_comprador+" "+self.comuna_comprador+" "+self.email_comprador+" "+self.pass_comprador
         return cadena
    
class Vendedor(models.Model):
    #Choices
    COMUNAS = (
        ('CE','Cerrillos'),
        ('CN','Cerro Navia'),
        ('CO','Conchalí'),
        ('EB','El Bosque'),
        ('EC','Estación Central'),
        ('HU','Huechuraba'),
        ('IN','Independencia'),
        ('LA','La Cisterna'),
        ('LF','La Florida'),
        ('LG','La Granja'),
        ('LP','La Pintana'),
        ('LR','La Reina'),
        ('LC','Las Condes'),
        ('LB','Lo Barnechea'),
        ('LE','Lo Espejo'),
        ('LP','Lo Prado'),
        ('MA','Macul'),
        ('MP','Maipú'),
        ('ÑU','Ñuñoa'),
        ('PH','Padre Hurtado'),
        ('PAC','Pedro Aguirre Cerda'),
        ('PE','Peñalolén'),
        ('PI','Pirque'),
        ('PR','Providencia'),
        ('PU','Pudahuel'),
        ('PA','Puente Alto'),
        ('QU','Quilicura'),
        ('QN','Quinta Normal'),
        ('REC','Recoleta'),
        ('REN','Renca'),
        ('SB','San Bernardo'),
        ('SJ','San Joaquín'),
        ('SJM','San José de Maipo'),
        ('SM','San Miguel'),
        ('SR','San Ramón'),
        ('SAN','Santiago'),
    )
    #Atributos
    id_vendedor = models.AutoField(primary_key=True)
    nombre_vendedor = models.CharField(max_length=30)
    apellido_vendedor = models.CharField(max_length=30)
    fono_vendedor = models.CharField(max_length=12)
    dir_vendedor = models.CharField(max_length=30)
    com_vendedor = models.TextField(max_length=3, choices=COMUNAS)
    email_vendedor = models.EmailField(max_length=25)
    usuario_vendedor = models.CharField(max_length=15)
    pass_vendedor = models.CharField(max_length=20)
   

    #Métodos
    #Retorna el nombre completo.
    def __str__(self): 
        return self.nombre_vendedor
   # def tostring(self):
      #  cadena=self. id_vendedor+" "+self.apellido_vendedor+" "+self.nombre_vendedor+" "+self.fono_vendedor+" "+self.dir_vendedor
      #  +" "+self.com_vendedor+" "+ self.email_vendedor+" "+self.pass_vendedor
       # return cadena

class DetalleCompra(models.Model):
    #Atributos
    id_compra = models.AutoField(primary_key=True, help_text="ID Compra")
    cant_prod = models.IntegerField(help_text="Cantidad de productos")
    monto_total = models.IntegerField(help_text="Monto a pagar")
    hora_compra = models.DateTimeField(max_length=30, help_text="Fecha y hora compra")
    comprador = models.ForeignKey('Comprador', on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)

    #Métodos
    #def __str__(self): 
    #    return self.id_compra
    def tostring(self):
         cadena=self.id_compra+" "+self.cant_prod+" "+self.monto_total+" "+self.hora_compra
         return cadena
    def total_pagar(self,Producto):
         total=self.cant_prod*Producto.precio_producto
         return total

class Producto(models.Model):
    #Choices
    UNIDAD_MEDIDA = (
        ('S','Kilogramo'),
        ('M','Gramo'),
        ('S','Unidad'),
        ('M','Docena'),
        ('S','Trozo'),
    )

    CATEGORIAS = (
        ('PA','Pasteles'),
        ('T','Torta'),
        ('G','Galletas'),
        ('B','Bollería'),
        ('CH','Chocolates'),
        ('B','Bombones'),
        ('PI','Pizza'),
        ('S','Sandwiches'),
        ('F','Frituras'),
        ('CO','Comida Oriental'),
    )
    
    #Atributos
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=25)
    precio_producto = models.IntegerField(help_text="Precio")
    descripcion_producto = models.TextField(max_length=25)
    unidad_medida = models.CharField(max_length=1, choices=UNIDAD_MEDIDA)
    categoria = models.CharField(max_length=2, choices=CATEGORIAS)
    imagen = models.ImageField(help_text="Foto producto")
    vendedor = models.ForeignKey('Vendedor', on_delete=models.SET_NULL, null=True)

    #Métodos
    def __str__(self): 
        return self.nombre_producto
    
    #def tostring(self):
      #  cadena=self. id_producto+" "+self.nombre_producto+" "+self.precio_producto+" "+self.descripcion_producto+" "
       # +self.categoria+" "+ self.imagen
       # return cadena

