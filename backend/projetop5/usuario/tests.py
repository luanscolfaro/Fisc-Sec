from django.test import TestCase
from usuario.models import Usuario

class UsuarioPermissaoTests(TestCase):
    def setUp(self):
        self.admin = Usuario.objects.create_user(
            username='admin',
            email='admin@example.com',
            password='adminpass',
            tipo_conta='admin',
            cpf='000.000.000-00'
        )

        self.servidor = Usuario.objects.create_user(
            username='servidor',
            email='servidor@example.com',
            password='servidorpass',
            tipo_conta='governo',
            cpf='111.111.111-11'
        )

        self.cidadao = Usuario.objects.create_user(
            username='cidadao',
            email='cidadao@example.com',
            password='cidadaopass',
            tipo_conta='cidadao',
            cpf='222.222.222-22'
        )

    def test_acesso_admin(self):
        self.assertEqual(self.admin.tipo_conta, 'admin')

    def test_acesso_servidor(self):
        self.assertEqual(self.servidor.tipo_conta, 'governo')

    def test_bloqueio_cidadao(self):
        self.assertEqual(self.cidadao.tipo_conta, 'cidadao')
