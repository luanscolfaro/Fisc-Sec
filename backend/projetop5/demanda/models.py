from django.db import models
from django.utils import timezone

class BaseModelQuerySet(models.QuerySet):
    def delete(self):
        self.update(deleted_at=timezone.now(), is_active=False)

class BaseManager(models.Manager):
    def get_queryset(self):
        return BaseModelQuerySet(self.model, using=self._db).filter(
            deleted_at__isnull=True,
            is_active=True
        )

class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)
    is_active = models.BooleanField(default=True, editable=False)

    objects = BaseManager()

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self, *args, **kwargs):
        super(BaseModel, self).delete(*args, **kwargs)


class Reclamacao(BaseModel):
    nome = models.CharField(max_length=100)  # futuramente pode ser substituído por FK para Usuario

    descricao = models.TextField()
    tipo_problema = models.CharField(max_length=100, default="Não especificado")
    endereco = models.TextField(null=True, blank=True)
    ponto_ref = models.TextField(blank=True, null=True)

    anexoone = models.ImageField(upload_to='anexos/', blank=True, null=True)
    anexotwo = models.ImageField(upload_to='anexos/', blank=True, null=True)

    URGENCIA_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]
    urgencia = models.CharField(
        max_length=10,
        choices=URGENCIA_CHOICES,
        default='media'
    )

    TIMELINE_CHOICES = [
        ('planejando', 'Planejando'),
        ('organizando', 'Organizando'),
        ('solucionando', 'Solucionando'),
        ('nao_resolvido', 'Não resolvido'),
        ('resolvido', 'Resolvido'),
    ]
    timeline = models.CharField(
        max_length=20,
        choices=TIMELINE_CHOICES,
        default='planejando'
    )

    def __str__(self):
        return f"Reclamação de {self.nome}"
