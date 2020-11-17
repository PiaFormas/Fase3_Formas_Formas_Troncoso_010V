from django.test import TestCase


#class ViewsTestCase(TestCase):
    #def test_index_loads_properly(self):
        #"""The index page loads properly"""
        #response = self.client.get('http://127.0.0.1:')
        #self.assertEqual(response.status_code, 200)

from categorias.models import Producto

class ViewProductos(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('http://127.0.0.1:8000/admin/categorias/producto/')
        self.assertEqual(response.status_code, 302)