from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Program, Scholarship
from .serializers import ProgramSerializer, ScholarshipSerializer
from django.http import Http404
from rest_framework import status, permissions

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
