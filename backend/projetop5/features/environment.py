import os
import django
from django.test.runner import DiscoverRunner

os.environ['DJANGO_SETTINGS_MODULE'] = 'projetop5.settings'
django.setup()

def before_all(context):
    """Configura Django antes de rodar os testes."""
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.client = django.test.Client()  # Cliente de teste do Django

def after_all(context):
    """Finaliza Django após os testes."""
    context.test_runner.teardown_test_environment()
