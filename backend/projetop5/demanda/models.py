from django.db import models
from django.utils import timezone

class BaseModelQuerySet(models.QuerySet):
    def delete(self):
        self.update(deleted_at=timezone.now(), is_active=False)

class BaseManager(models.Manager):
    def get_queryset(self):
        return BaseModelQuerySet(self.model, using=self._db).filter(
            deleted_at__isnull=True, is_active=True
        )

class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(editable=False, blank=True, null=True)
    is_active = models.BooleanField(editable=False, default=True)

    objects = BaseManager()

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self, *args, **kwargs):
        super(BaseModel, self).delete(*args, **kwargs)

class Reclamacao(BaseModel):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    descricao = models.TextField()

    def __str__(self):
        return f"Reclamação de {self.nome}"