from django.db import models

from experiment.models import Variant, Experiment


class Batch(models.Model):
    PENDING = 0
    COMMITTED = 1
    STATUS = (
        (PENDING, "pending"),
        (COMMITTED, "committed")
    )

    udid = models.CharField(max_length=128, unique=True, verbose_name="udid")
    status = models.SmallIntegerField(choices=STATUS, verbose_name="status")
    experiment = models.ForeignKey(Experiment, name="experiment", on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, name="variant", on_delete=models.CASCADE)
    assign_timestamp = models.DateTimeField(verbose_name="assigned_at")
    commit_timestamp = models.DateTimeField(verbose_name="committed_at")
    batch_id = models.CharField(verbose_name="batch_id")


class Cache(models.Model):

    udid = models.CharField(max_length=128)
    experiment = models.ForeignKey(Experiment, name="experiment", on_delete=models.CASCADE)
    batches = models.ManyToManyField(Batch, verbose_name="batches")
    first_batch = models.ForeignKey(Batch, verbose_name="first_batch", on_delete=models.CASCADE)
    last_batch = models.ForeignKey(Batch, verbose_name="last_batch", on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, name="variant", on_delete=models.CASCADE)
    exposure_counts = models.BigIntegerField(name="exposure_counts")

