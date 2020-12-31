from datetime import datetime

from django.db import DatabaseError, transaction
from django.db.models import Max

from .models import Cache, Batch


class Assignment:

    def assign(self):
        pass

    def commit(self):
        pass


class BatchGenerator:

    def get_batch_id(self):
        return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    def generate(self, experiment: str, candidates: list) -> str:
        batch_id = self.get_batch_id()
        snapshot = set(self.get_snapshot(experiment))
        new_audience = [udid for udid in candidates if udid not in snapshot]
        self.load_new_audience(new_audience, experiment, batch_id)
        return batch_id

    def commit(self, batch_id, action):
        target_batch: QuerySet = Batch.objects.filter(batch_id=batch_id)
        for audience in target_batch:
            try:
                action(audience)
                audience.commit_timestamp = None
                audience.status = Batch.COMMITTED
                with transaction.atomic():
                    audience.save()
            except DatabaseError:
                # Do something to reverse action if needed.
                continue

    def get_snapshot(self, experiment: str):
        committed_audience = Cache.objects.all().filter(experiment=experiment)
        largest_batch = committed_audience.aggregate(Max("batch_id"))["batch_id"]
        snapshot = committed_audience.filter(batch_id=largest_batch).only("udid").values_list(flat=True)
        return snapshot

    def load_new_audience(self, new_audience: list, experiment: str, batch_id: str) -> str:
        variants = self.get_or_create_variant(experiment)
        assigned_variants = self.assign_variant(len(new_audience), variants)
        for audience, variant in zip(new_audience, assigned_variants):
            _audience = Batch(udid=audience["udid"],
                              status=Batch.PENDING,
                              experiment=experiment,
                              variant=variants[variant],
                              assign_timestamp=datetime.now(),
                              batch_id=batch_id)
            try:
                with transaction.atomic():
                    _audience.save()
            except DatabaseError:
                pass  # do something about it

        return batch_id

    def get_or_create_variant(self, experiment: str) -> dict:
        pass


    def assign_variant(self, counts: int, variants: dict) -> list:
        pass