
from django.db import models


class Hombres(models.Manager):
    def get_queryset(self):
        return super(Hombres, self).get_queryset().filter(tipo="Pastas")

