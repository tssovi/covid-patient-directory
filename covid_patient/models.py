import logging
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Patient(models.Model):
    patient_id = models.PositiveSmallIntegerField(primary_key=True)
    patient_name = models.CharField(max_length=150, null=False)
    patient_age = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(int(0)), MaxValueValidator(int(120))])
    patient_address = models.CharField(max_length=250, null=True)
    patient_phone = models.CharField(max_length=150, null=True)
    patient_status = models.CharField(max_length=50, null=False)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_id} - {self.patient_name} - {self.patient_status}"