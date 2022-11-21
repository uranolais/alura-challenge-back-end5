from django.db import models


class Video(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    url = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.titulo
