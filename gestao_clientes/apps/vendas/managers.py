from django.db import models
from django.db.models import Avg, Min, Max, Count


class SaleManager(models.Manager):

    def average(self):
        return self.all().aggregate(Avg('value'))['value__avg']

    def discount__avg(self):
        return self.all().aggregate(Avg('discount'))['discount__avg']

    def value__min(self):
        return self.all().aggregate(Min('value'))['value__min']

    def value_max(self):
        return self.all().aggregate(Max('value'))['value__max']

    def count_id(self):
        return self.all().aggregate(Count('id'))['id__count']

    def count_nf_submit(self):
        return self.filter(nfe_issued=True).aggregate(Count('id'))['id__count']
