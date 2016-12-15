from django.db import models


class Pytania(models.Model):
    pytanie = models.TextField()
    odpowiedz = models.TextField()
    user = models.CharField(max_length=100)
    carddeck = models.CharField(max_length=100)

    def __str__(self):
        return (self.user, self.carddeck,self.pytanie)



