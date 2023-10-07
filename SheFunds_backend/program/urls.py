from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('program', views.ProgramList.as_view()),
    path('scholarship', views.ScholarshipList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)