from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from covid_patient.models import Patient
from covid_patient.serializers import PatientSerializer


class AddPatient(APIView):
    permission_classes = [AllowAny]
    # Insert Patient Data
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(
                {
                    'data': data,
                    'message': 'Patient Details Inserted Successfully',
                    'response_code': "DIS-201"
                }, status=status.HTTP_201_CREATED
            )

        else:
            data = serializer.errors
            return Response(
                {
                    'data': data,
                    'message': 'Invalid Request',
                    'response_code': "IVR-400"
                }, status=status.HTTP_400_BAD_REQUEST
            )


class PatientList(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        roles = Patient.objects.all().order_by('patient_id')
        serializer = PatientSerializer(roles, many=True)
        data = serializer.data
        return Response(
            {
                'data': data,
                'message': 'Patient List Found Successfully',
                'response_code': "DFS-200"
            }, status=status.HTTP_200_OK
        )


class PatientDetails(APIView):
    permission_classes = [AllowAny]
    """Update, delete and get single Patient"""

    def get(self, request, patient_id):
        patient = get_object_or_404(Patient, patient_id=patient_id)
        serializer = PatientSerializer(patient, many=False)
        data = serializer.data
        return Response(
            {
                'data': data,
                'message': 'Patient Details Data Found Successfully',
                'response_code': "DFS-200"
            }, status=status.HTTP_200_OK
        )


class UpdatePatient(APIView):
    permission_classes = [AllowAny]
    def put(self, request, patient_id):
        patient = get_object_or_404(Patient, patient_id=patient_id)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(
                {
                    'data': data,
                    'message': 'Patient Details Updated Successfully',
                    'response_code': "DUS-202"
                }, status=status.HTTP_202_ACCEPTED
            )
        else:
            data = serializer.errors
            return Response(
                {
                    'data': data,
                    'message': 'Invalid Request',
                    'response_code': "IVR-400"
                }, status=status.HTTP_400_BAD_REQUEST
            )


class DeletePatient(APIView):
    permission_classes = [AllowAny]
    def delete(self, request, patient_id):
        patient = get_object_or_404(Patient, patient_id=patient_id)
        patient.delete()
        return Response(
            {
                'patient_id': patient_id,
                'message': 'Patient Deleted Successfully',
                'response_code': "DDS-202"
            }, status=status.HTTP_202_ACCEPTED
        )


class DeleteRecoveredPatient(APIView):
    permission_classes = [AllowAny]
    def delete(self, request):
        recovered_patient = Patient.objects.filter(patient_status="recovered")
        recovered_patient.delete()
        return Response(
            {
                'message': 'All Recovered Patient Deleted Successfully',
                'response_code': "DDS-202"
            }, status=status.HTTP_202_ACCEPTED
        )
