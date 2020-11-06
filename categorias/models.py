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
    id_comprador = models.AutoField(primary_key=True, help_text="ID Comprador")
    nombre_comprador = models.TextField(max_length=30, help_text="Nombre Comprador")
    apellido_comprador = models.TextField(max_length=30, help_text="Apellido Comprador")
    fono_comprador = models.CharField(max_length=12, help_text="Fono Comprador")
    dir_comprador = models.CharField(max_length=30, help_text="Dirección Comprador")
    comuna_comprador = models.CharField(max_length=3, choices=COMUNAS, help_text="Comuna Comprador")
    email_comprador = models.EmailField(max_length=25, help_text="E-mail Comprador")
    pass_comprador = models.CharField(max_length=20, help_text="Password Comprador")
 

    #Métodos
    def __str__(self): 
         return self.nombre_comprador
    def tostring(self):
         cadena=self.id_comprador+" "+self.apellido_comprador+" "+self.nombre_comprador+" "+self.fono_comprador+" "+self.dir_comprador+" "
         +self.comuna_comprador+" "+self.email_comprador+" "+self.pass_comprador
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
    id_vendedor = models.AutoField(primary_key=True, help_text="ID Vendedor")
    nombre_vendedor = models.TextField(max_length=30, help_text="Nombre Vendedor")
    apellido_vendedor = models.TextField(max_length=30, help_text="Apellido Vendedor")
    fono_vendedor = models.CharField(max_length=12, help_text="Fono Vendedor")
    dir_vendedor = models.CharField(max_length=30, help_text="Dirección Vendedor")
    com_vendedor = models.TextField(max_length=3, choices=COMUNAS, help_text="Comuna Vendedor")
    email_vendedor = models.EmailField(max_length=25, help_text="E-mail Vendedor")
    pass_vendedor = models.CharField(max_length=20, help_text="Password Vendedor")
   

    #Métodos
    #Retorna el nombre completo.
    def __str__(self): 
        return self.nombre_vendedor
    def tostring(self):
        cadena=self. id_vendedor+" "+self.apellido_vendedor+" "+self.nombre_vendedor+" "+self.fono_vendedor+" "+self.dir_vendedor
        +" "+self.com_vendedor+" "+ self.email_vendedor+" "+self.pass_vendedor
        return cadena

class DetalleCompra(models.Model):
    #Atributos
    id_compra = models.AutoField(primary_key=True, help_text="ID Compra")
    cant_prod = models.IntegerField(help_text="Cantidad de productos")
    monto_total = models.IntegerField(help_text="Monto a pagar")
    hora_compra = models.DateTimeField(max_length=30, help_text="Fecha y hora compra")
    comprador = models.ForeignKey('Comprador', on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)

    #Métodos
    def __str__(self): 
         return self.id_compra
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
    id_producto = models.AutoField(primary_key=True, help_text="ID Producto")
    nombre_producto = models.TextField(max_length=25, help_text="Nombre del producto")
    precio_producto = models.IntegerField(help_text="Precio")
    descripcion_producto = models.TextField(max_length=25, help_text="Nombre del producto")
    unidad_medida = models.CharField(max_length=1, choices=UNIDAD_MEDIDA, help_text="Unidad de medida")
    categoria = models.CharField(max_length=2, choices=CATEGORIAS, help_text="Categoría")
    imagen = models.ImageField(help_text="Foto producto")
    vendedor = models.ForeignKey('Vendedor', on_delete=models.SET_NULL, null=True)

    #Métodos
    def __str__(self): 
        return self.nombre_producto
    
    def tostring(self):
        cadena=self. id_producto+" "+self.nombre_producto+" "+self.precio_producto+" "+self.descripcion_producto+" "+self.unidad_medida
        +" "+self.categoria+" "+ self.imagen
        return cadena

class Tarjeta(models.Model):
    BANCO = (
        ('S','Banco Bci'),
        ('M','Banco de Chile'),
        ('S','Banco Estado'),
        ('M','Banco Santander'),
        ('S','Banco BICE'),
        ('M','Banco Condell'),
        ('S','Banco CrediChile'),
        ('M','Banco Edwards Citi'),
        ('S','Banco Falabella'),
        ('M','Banco Internacional'),
        ('S','Banco Itaú'),
        ('M','Banco Ripley'),
        ('S','Banco Security'),
        ('M','Scotiabank'),
    )
       
    
    #Atributos
    id_tarjeta = models.AutoField(primary_key=True, help_text="ID Tarjeta")
    nro_tarjeta = models.IntegerField(help_text="Nro Tarjeta")
    nombre_titular = models.TextField(max_length=25, help_text="Nombre del titular de la tarjeta")
    banco = models.TextField(max_length=1, choices=BANCO, help_text="Nombre del banco")
    mes_vencimiento = models.CharField(max_length=2, help_text="Mes de vencimiento")
    anno_vencimiento = models.CharField(max_length=4, help_text="Año de vencimiento")
    comprador = models.OneToOneField(
        Comprador,
        on_delete=models.CASCADE,
      
    )
    
    #Métodos
    def __str__(self): 
        return self.nro_tarjeta
    #def tostring(self):
       # cadena=self. id_tarjeta+" "+self.nro_tarjeta+" "+self.nombre_titular+" "+self.banco+" "+self.mes_vencimiento
       # +" "+self.anno_vencimiento
       # return cadena

class CuentaBanco(models.Model):
    BANCO = (
        ('S','Banco Bci'),
            ('M','Banco de Chile'),
        ('S','Banco Estado'),
            ('M','Banco Santander'),
        ('S','Banco BICE'),
            ('M','Banco Condell'),
        ('S','Banco CrediChile'),
            ('M','Banco Edwards Citi'),
        ('S','Banco Falabella'),
            ('M','Banco Internacional'),
        ('S','Banco Itaú'),
            ('M','Banco Ripley'),
        ('S','Banco Security'),
        ('M','Scotiabank'),
        )
    TIPOCUENTA = (
        ('CC','Cuenta Corriente'),
        ('CV','Cuenta Vista'),
        ('CR', 'Cuenta Rut'),

    )
        
    #Atributos
    id_cuenta = models.AutoField(primary_key=True, help_text="ID cuenta")
    nro_cuenta = models.IntegerField(help_text="Nro cuenta")
    nombre_titular = models.TextField(max_length=25, help_text="Nombre del titular de la cuenta")
    banco = models.TextField(max_length=1, choices=BANCO, help_text="Nombre del banco")
    tipo_cuenta = models.CharField(max_length=20, help_text="Tipo de cuenta", choices=TIPOCUENTA)
    email_titular = models.EmailField(max_length=25, help_text="E-mail titular")
    rut_titular = models.CharField(max_length=10, help_text="Rut titular")
    vendedor = models.OneToOneField(
        Vendedor,
        on_delete=models.CASCADE,
        
    )
     
    
    #Métodos
    def __str__(self): 
        num=str(self.nro_cuenta)
        return num


   #def tostring(self):
        #cadena=self. id_cuenta+" "+self.nro_cuenta+" "+self.nombre_titular+" "+self.banco+" "+self.tipo_cuenta
       # +" "+self.email_titular+" "+ self.rut_titular
        #return cadena


 
   
