from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Program, Scholarship, Applicant
from .serializers import ProgramSerializer, ScholarshipSerializer, ApplicantSerializer, ProgramDetailSerializer, ApplicantDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
import datetime 
from django.core.mail import send_mail
from django.conf import settings

class ProgramList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        program = Program.objects.all()
        serializer = ProgramSerializer(program, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProgramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class ProgramDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):

        try: 
            program = Program.objects.get(pk=pk)
            self.check_object_permissions(self.request, program)
            return program
        except Program.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        program = self.get_object(pk) 
        #serializer = ProgramSerializer(Program)
        serializer = ProgramDetailSerializer(program)        
        return Response(serializer.data)
    
    def put(self, request, pk):
        program = self.get_object(pk)

        serializer = ProgramDetailSerializer(
            instance=program,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )   
    
    def delete(self, request, pk):
        program = self.get_object(pk)
        program.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT 
        )     

class ProgramOpenList(APIView):

    def get(self, request):
        program = Program.objects.all()
        today_date = datetime.datetime.now().date()
        filter_open_program = program.filter(
                application_date_start__lte=today_date, 
                application_date_end__gte=today_date
            )        
        serializer = ProgramSerializer(filter_open_program, many=True)
        return Response(serializer.data)

class ScholarshipList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        scholarship = Scholarship.objects.all()
        serializer = ScholarshipSerializer(scholarship, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ScholarshipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ScholarshipDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            scholarship = Scholarship.objects.get(pk=pk)
            self.check_object_permissions(self.request, scholarship)
            return scholarship
        except Scholarship.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        scholarship = self.get_object(pk)
        serializer = ScholarshipSerializer(scholarship)
        return Response(serializer.data)
    
    def put(self, request, pk):
        scholarship = self.get_object(pk)
        serializer = ScholarshipSerializer(
            instance=scholarship,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
            )

    def delete(self, request, pk):
        scholarship = self.get_object(pk)
        scholarship.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ApplicantList(APIView):
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #commenting the above out as posting of applicant requires no permission

    def get(self, request):
        applicant = Applicant.objects.all()
        serializer = ApplicantSerializer(applicant, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ApplicantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                subject='She Codes Application Received', 
                message='Thank you for your application, we will be in touch soon!', 
                from_email=settings.EMAIL_HOST_USER, 
                recipient_list=[request.data['email']],
                fail_silently=False,
            )            
            
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class ApplicantDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):

        try: 
            applicant = Applicant.objects.get(pk=pk)
            self.check_object_permissions(self.request, applicant)
            return applicant
        except Applicant.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        applicant = self.get_object(pk) 
        serializer = ApplicantDetailSerializer(applicant)        
        return Response(serializer.data)
    
    def put(self, request, pk):
        applicant = self.get_object(pk)

        serializer = ApplicantDetailSerializer(
            instance=applicant,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )   
    
    def delete(self, request, pk):
        applicant = self.get_object(pk)
        applicant.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT 
        )         