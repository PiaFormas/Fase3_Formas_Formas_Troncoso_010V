from django.test import TestCase
from categorias.models import Vendedor 

class ModelsTestCase(TestCase):
  
    def setUp(self):
        Vendedor.objects.create(nombre_vendedor="Rosita", apellido_vendedor="Perez",
        fono_vendedor = "93345635", dir_vendedor= "Los ceibos 2222", com_vendedor = "Puente Alto",
        email_vendedor = "rosaperez@gmail.com", usuario_vendedor = "rosape", pass_vendedor = "asd123456")

        Vendedor.objects.create(nombre_vendedor="Carmelo", apellido_vendedor="Weiler",
        fono_vendedor = "93367635", dir_vendedor= "Los casos 333", com_vendedor = "La Granja",
        email_vendedor = "carweiler@gmail.com", usuario_vendedor = "carmelo23", pass_vendedor = "asd123456")

    
    def test_nombre_y_apellido(self):
        """Devuelve el nombre completo del vendedor correctamente"""
        vendedor = Vendedor.objects.get(nombre_vendedor="Rosita")
        nombre_object_esperado = vendedor.nombre_vendedor+" "+vendedor.apellido_vendedor
        self.assertEqual(nombre_object_esperado, str(vendedor))

        vendedor = Vendedor.objects.get(nombre_vendedor="Carmelo")
        nombre_object_esperado = vendedor.nombre_vendedor+" "+vendedor.apellido_vendedor
        self.assertEqual(nombre_object_esperado, str(vendedor))
