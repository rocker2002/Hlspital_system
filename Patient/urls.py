from django.urls import path

from Patient.views import PatientListView

urlpatterns = [
    path('<int:pk>/', PatientListView.as_view(), name='patient'),
]