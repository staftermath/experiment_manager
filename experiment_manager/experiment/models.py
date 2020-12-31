from django.db import models

from account.models import Team


class Category(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    type = models.CharField(max_length=32, verbose_name="type")

    def __str__(self):
        return f"{self.team.name}: {self.type}"


class Tag(models.Model):

    name = models.CharField(max_length=64, verbose_name="tag")
    description = models.TextField(max_length=1024, verbose_name="description")

    def __str__(self):
        return self.name


class Treatment(models.Model):

    name = models.CharField(max_length=128, verbose_name="name")
    tags = models.ManyToManyField(Tag, verbose_name="tags")

    def __str__(self):
        return self.name


class Variant(models.Model):

    id = models.AutoField()
    name = models.CharField(max_length=256, verbose_name="name")
    percentage = models.DecimalField(max_digits=6, decimal_places=4, verbose_name="percentage")
    treatments = models.ManyToManyField(Treatment, verbose_name="treatments")

    def __str__(self):
        return self.name


class Experiment(models.Model):

    name = models.CharField(max_length=128, verbose_name="name", primary_key=True)
    start_datetime = models.DateTimeField(verbose_name="start time", editable=True)
    end_datetime = models.DateTimeField(verbose_name="end time", editable=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    variants = models.ManyToManyField(Variant, verbose_name="variants")
    description = models.TextField(max_length=1024, verbose_name="description")
    doc = models.URLField(verbose_name="doc link")
    config = models.JSONField(verbose_name="config", default=dict(), blank=True)

    def __str__(self):
        return self.name
