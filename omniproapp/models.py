from django.db import models

class BaselineProfileModel(models.Model):
    baseline_file = models.FileField(upload_to='baselines/%Y%m%d', null=True)

class MeasuredProfileModel(models.Model):
    measurement_file = models.FileField(upload_to='measurements/%Y%m%d', null=True)