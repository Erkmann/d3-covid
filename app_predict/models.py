from django.db import models


class Dia(models.Model):
    data = models.DateField(null=False, blank=False)
    casos = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f'{self.data} | {self.casos}'
