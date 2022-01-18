from rest_framework import viewsets
from media.serializer import StockSerializer
from media.models import Filem


class StockViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Filem.objects.all().order_by('film_name')
    serializer_class = StockSerializer  # Сериализатор для модели