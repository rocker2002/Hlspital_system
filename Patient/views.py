from rest_framework import generics, mixins
from rest_framework.response import Response

from Patient.models import Patient
from Patient.serializers import PatientSerializer


class PatientListView(generics.GenericAPIView, mixins.CreateModelMixin,
                      mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)




