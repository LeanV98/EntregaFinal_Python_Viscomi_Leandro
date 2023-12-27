from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from PaginaWeb.models import Avatar

class PaginaTestCase(TestCase):
    def setUp(self):
        # Configuración común para las pruebas
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@example.com')
        self.avatar = Avatar.objects.create(user=self.user, imagen='path/to/test/image.jpg')

    def test_edicion_perfil(self):
        # Inicia sesión
        self.client.login(username='testuser', password='testpassword')

        # Accede a la vista EditarPerfil
        response = self.client.get(reverse('EditarPerfil'))
        self.assertEqual(response.status_code, 200)  # Verifica que se pueda acceder a la vista

        # Realiza una edición en el perfil (ajusta los datos según tus necesidades)
        response = self.client.post(
            reverse('EditarPerfil'),
            {'username': 'testuser', 'first_name': 'NuevoNombre', 'last_name': 'NuevoApellido', 'email': 'test@example.com'}
        )

        # Verifica que la edición fue exitosa (código 302 significa redirección)
        self.assertIn(response.status_code, [200, 302])

        # Si hay redirección, sigue la redirección
        if response.status_code == 302:
            response = self.client.get(response.url)
            self.assertEqual(response.status_code, 200)  # Verifica el código después de la redirección

        # Obtiene el usuario actualizado desde la base de datos
        user_actualizado = User.objects.get(username='testuser')

        # Verifica que los cambios se hayan aplicado correctamente
        self.assertEqual(user_actualizado.first_name, 'NuevoNombre')
        self.assertEqual(user_actualizado.last_name, 'NuevoApellido')

        # Verifica que la imagen del avatar no se haya modificado (opcional)
        avatar_actualizado = Avatar.objects.get(user=user_actualizado)
        self.assertEqual(avatar_actualizado.imagen, 'path/to/test/image.jpg')