from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('program', views.ProgramList.as_view()),
    path('program-open', views.ProgramOpenList.as_view()),
    path('program/<int:pk>', views.ProgramDetail.as_view()),    
    path('scholarship', views.ScholarshipList.as_view()),
    path('scholarship/<int:pk>', views.ScholarshipDetail.as_view()),
    path('applicant', views.ApplicantList.as_view()),
    path('applicant/<int:pk>', views.ApplicantDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)