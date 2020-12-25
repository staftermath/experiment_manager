from django.db import models


class Category(models.Model):
    MARKETING = 0
    PRODUCT = 1
    TEAMS = (
        (MARKETING, "marketing"),
        (PRODUCT, "product")
    )

    team = models.PositiveIntegerField(default=MARKETING, choices=TEAMS, verbose_name="team")
    type = models.CharField(max_length=32, verbose_name="type")


class Experiment(models.Model):

    name = models.CharField(max_length=128, verbose_name="name")
    start_datetime = models.DateTimeField(auto_now_add=True, verbose_name="start time")
    end_datetime = models.DateTimeField(verbose_name="end time")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField(max_length=1024, verbose_name="description")
    doc = models.URLField(verbose_name="doc link")
    config = models.JSONField(verbose_name="config")


class Tag(models.Model):

    name = models.CharField(max_length=64, verbose_name="tag")
    description = models.TextField(max_length=1024, verbose_name="description")


class Treatment(models.Model):

    name = models.CharField(max_length=128, verbose_name="name")
    tags = models.ManyToManyField(Tag, verbose_name="tags")


class Variant(models.Model):

    name = models.CharField(max_length=256, verbose_name="name")
    percentage = models.DecimalField(max_digits=6, decimal_places=4, verbose_name="percentage")
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    treatments = models.ManyToManyField(Treatment, verbose_name="treatments")
