
from django.db import models


class Pasta(models.Manager):
    def get_queryset(self):
        return super(Pasta, self).get_queryset().filter(tipo="Pastas")

