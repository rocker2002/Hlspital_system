from django.urls import path

from Patient.views import PatientListView

urlpatterns = [
    path('', PatientListView.as_view(), name='patient'),
]