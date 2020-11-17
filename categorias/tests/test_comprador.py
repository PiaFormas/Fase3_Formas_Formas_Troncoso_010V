from django.test import TestCase
from categorias.models import Comprador

class ModelsTestCase(TestCase):
  
    def setUp(self):
        Comprador.objects.create(nombre_comprador="Juan", apellido_comprador="Rojas",
        fono_comprador = "93345632", dir_comprador= "Los paltos 1111", comuna_comprador = "Cerrillos",
        email_comprador = "juanrojas@gmail.com", usuario_comprador = "jurojas", pass_comprador = "asd123456")

        Comprador.objects.create(nombre_comprador="Vicky", apellido_comprador="Luna",
        fono_comprador = "93235632", dir_comprador= "Rengifo 1231", comuna_comprador = "Santiago",
        email_comprador = "vickylu@gmail.com", usuario_comprador = "vicluna", pass_comprador = "asd123456")

    def test_nombre_y_apellido(self):
        """Devuelve el nombre completo del comprador correctamente"""
        comprador = Comprador.objects.get(nombre_comprador="Juan")
        nombre_object_esperado = comprador.nombre_comprador+" "+comprador.apellido_comprador
        self.assertEqual(nombre_object_esperado, str(comprador))

        comprador = Comprador.objects.get(nombre_comprador="Vicky")
        nombre_object_esperado = comprador.nombre_comprador+" "+comprador.apellido_comprador
        self.assertEqual(nombre_object_esperado, str(comprador))

