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

class ProgramDetailSerializer(ProgramSerializer):
    scholarship = ScholarshipSerializer(many=True, read_only=True)     

    def update(self, instance, validated_data):
        instance.program_name = validated_data.get('program_name', instance.program_name)
        instance.location = validated_data.get('location', instance.location)
        instance.intake = validated_data.get('intake', instance.intake)                
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.status = validated_data.get('status', instance.status)
        instance.date_start = validated_data.get('date_start', instance.date_start)        
        instance.date_end = validated_data.get('date_end', instance.date_end)
        instance.application_date_start = validated_data.get('application_date_start', instance.application_date_start)        
        instance.application_date_end = validated_data.get('application_date_end', instance.application_date_end)
        instance.save()
        return instance
