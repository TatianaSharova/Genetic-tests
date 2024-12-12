from django_filters.rest_framework import FilterSet, filters

from gentests.models import Test


class TestFilter(FilterSet):
    '''Фильтр по видам животных для модели Test.'''
    species = filters.CharFilter(field_name='species', lookup_expr='iexact')

    class Meta:
        model = Test
        fields = ['species']
