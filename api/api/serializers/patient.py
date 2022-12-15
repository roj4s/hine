from rest_framework import serializers
from ..models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'birthdate', 'gender', 'nationality', 'fathers_name',
                  'fathers_age', 'fathers_profession', 'fathers_schooling',
                  'family_income', 'address', 'phone', 'cns', 'cpf', 'rg',
                  'review_date', 'clinical_diagnosis',
                  'physiotherapist_in_charge', 'academic_in_charge']
