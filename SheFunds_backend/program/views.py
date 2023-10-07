from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Program
from .serializers import ProgramSerializer
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
