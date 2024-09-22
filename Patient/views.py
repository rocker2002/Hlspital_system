from rest_framework import generics, mixins
from rest_framework.response import Response

from Patient.models import Patient
from Patient.serializers import PatientSerializer


class PatientListView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)




