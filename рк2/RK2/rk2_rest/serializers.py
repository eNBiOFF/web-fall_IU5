from rest_framework import serializers
from rk2_rest.models import Musicians, Orchestrys


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musicians
        fields = ['id', 'name', 'role', 'id_orkestry']


class OrchestrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Orchestrys
        fields = ['id', 'name']
