from django.contrib.auth.models import User
from django.db import models
from django.db.models import Index
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ["name"]

        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, blank=True, null=True, related_name="cities"
    )

    class Meta:
        ordering = ["name"]

        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self):
        return self.name


class Dealer(User):
    title = models.CharField(max_length=100)
    email = models.CharField(max_length=55, blank=True, unique=True)
    city = models.ForeignKey(
        City, on_delete=models.DO_NOTHING, blank=False, related_name="dealers"
    )

    class Meta:
        indexes = [Index(fields=("title",))]

        verbose_name = _("Dealer")
        verbose_name_plural = _("Dealers")

    def __str__(self):
        return self.title
