from django.test import TestCase
from categorias.forms import VendedorForm


class TestForms(TestCase):

    #def test_vendedor_form_datos_validos(self):
        #form = VendedorForm(data={
        #    'id_vendedor': '12',
        #    'nombre_vendedor': 'Mirko',
        #    'apellido_vendedor': 'Ramirez',
        #    'fono_vendedor': '123456778',
        #    'dir_vendedor': 'Los gallos 345',
        #    'com_vendedor': 'La Cisterna',
        #    'email_vendedor': 'mirko@gmail.com',
        #    'usuario_vendedor': 'mirram123',
        #    'pass_vendedor': 'ayuwoki123'
        #})

        #self.assertTrue(form.is_valid())
    
    def test_vendedor_form_nombre_invalido(self):
        form = VendedorForm(data={'nombre_vendedor': '34#q10'})
        self.assertFalse(form.is_valid())
    
    def test_vendedor_form_apellido_invalido(self):
        form = VendedorForm(data={'apellido_vendedor': '34#q10'})
        self.assertFalse(form.is_valid())
    
    def test_vendedor_form_email_invalido(self):
        form = VendedorForm(data={'email_vendedor': 'gmail123'})
        self.assertFalse(form.is_valid())

    def test_vendedor_form_sin_datos(self):
        form = VendedorForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 8)