from media.models import Filem
from rest_framework import serializers


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Filem
        # Поля, которые мы сериализуем
        fields = ["pk", "film_name", "description"]