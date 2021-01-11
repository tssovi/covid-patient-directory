from rest_framework import serializers
from covid_patient.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['patient_id', 'patient_name', 'patient_age', 'patient_address', 'patient_phone', 'patient_status']

