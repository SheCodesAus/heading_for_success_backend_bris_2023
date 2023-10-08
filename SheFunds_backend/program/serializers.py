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

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('program.Applicant')
        fields = '__all__'         

class ProgramDetailSerializer(ProgramSerializer):
    scholarship = ScholarshipSerializer(many=True, read_only=True)     
    applicant = ApplicantSerializer(many=False, read_only=True) 

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

class ApplicantDetailSerializer(ApplicantSerializer):

    def update(self, instance, validated_data):
        # instance.first_name = validated_data.get('first_name', instance.first_name)
        # instance.last_name = validated_data.get('last_name', instance.last_name)        
        # instance.email = validated_data.get('email', instance.email)
        # instance.age = validated_data.get('age', instance.age)
        # instance.contact_mobile = validated_data.get('contact_mobile', instance.contact_mobile)        
        # instance.location = validated_data.get('location', instance.location)
        # instance.reason = validated_data.get('reason', instance.reason)                
        # instance.previous_education = validated_data.get('previous_education', instance.previous_education)
        # instance.work_experience = validated_data.get('work_experience', instance.work_experience)
        # instance.currently_employed = validated_data.get('currently_employed', instance.currently_employed)                
        # instance.current_employer = validated_data.get('current_employer', instance.current_employer)
        # instance.biography = validated_data.get('biography', instance.biography)        
        # instance.gender_eligible = validated_data.get('gender_eligible', instance.gender_eligible)
        # instance.resume = validated_data.get('resume', instance.resume)           
        instance.status = validated_data.get('status', instance.status)
        instance.scholarship = validated_data.get('scholarship', instance.scholarship)        
        instance.save()
        return instance