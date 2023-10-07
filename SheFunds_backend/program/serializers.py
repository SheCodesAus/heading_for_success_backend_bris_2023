from rest_framework import serializers
from django.apps import apps

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('program.Program')
        fields = '__all__'

class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('program.Scholarship')
        fields = '__all__'