from django.shortcuts import render
from rest_framework import viewsets

from rk2_rest.models import Musicians, Orchestrys
from rk2_rest.serializers import MusicianSerializer, OrchestrySerializer
# Create your views here.


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musicians.objects.all()
    serializer_class = MusicianSerializer


class OrchestryViewSet(viewsets.ModelViewSet):
    queryset = Orchestrys.objects.all()
    serializer_class = OrchestrySerializer


def report(req):
    return render(req, 'report.html', {
        "data": Musicians.objects.all(),
        "dataork": Orchestrys.objects.all()
    })