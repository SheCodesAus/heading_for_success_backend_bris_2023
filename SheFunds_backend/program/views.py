from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Program, Scholarship
from .serializers import ProgramSerializer, ScholarshipSerializer
from django.http import Http404
from rest_framework import status, permissions
import datetime 

class ProgramList(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
    def get_object(self, pk):
        try:
            return Scholarship.objects.get(pk=pk)
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
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        scholarship = self.get_object(pk)
        scholarship.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
