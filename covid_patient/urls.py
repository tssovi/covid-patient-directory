from django.urls import path
from covid_patient.views import *

app_name = "covid_patient"

urlpatterns = [
    path('add-patient/', AddPatient.as_view(), name='add-patient'),
    path('patient-list/', PatientList.as_view(), name='patient-list'),
    path('patient-details/<int:patient_id>/', PatientDetails.as_view(), name='patient-details'),
    path('update-patient/<int:patient_id>/', UpdatePatient.as_view(), name='update-patient'),
    path('delete-patient/<int:patient_id>/', DeletePatient.as_view(), name='delete-patient'),
    path('delete-recovered-patient/', DeleteRecoveredPatient.as_view(), name='delete-recovered-patient'),
]
