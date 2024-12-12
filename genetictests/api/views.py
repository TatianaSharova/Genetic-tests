from django.db.models import Avg, Count, Max, Q
from django.db.models.functions import Round
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import TestFilter
from .serializers import StatisticsSerializer, TestSerializer
from gentests.models import Test


class TestViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    '''VeiwSet для просмотра и создания генетических тестов.'''
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = TestFilter

    def create(self, request, *args, **kwargs):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            test = serializer.save()
            return Response({'message': 'Данные успешно добавлены.',
                             'id': test.id}, status=status.HTTP_201_CREATED)
        return Response({'field_name': serializer.errors})


class StatisticsView(APIView):
    '''View для просмотра статистики.'''

    @extend_schema(
        responses={status.HTTP_200_OK: StatisticsSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        statistics = (
            Test.objects
            .values('species')
            .annotate(
                total_tests=Count('id'),
                avg_milk_yield=Round(Avg('milk_yield'), 1),
                max_milk_yield=Max('milk_yield'),
                good_health_percentage=Count('id', filter=Q(
                    health_status='good'
                    )) * 100 / Count('id')
            )
        )
        serializer = StatisticsSerializer(statistics, many=True)
        return Response({'statistics': serializer.data})
