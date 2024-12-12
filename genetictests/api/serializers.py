import datetime as dt

from django.core.exceptions import ValidationError
from rest_framework import serializers

from gentests.models import Test


class TestSerializer(serializers.ModelSerializer):
    '''Serializer для добавления и чтения тестов.'''
    milk_yield = serializers.FloatField(min_value=0.0)

    class Meta:
        model = Test
        fields = ('id', 'animal_name', 'species',
                  'test_date', 'milk_yield', 'health_status')

    def validate_test_date(self, data):
        '''
        Валидация даты, когда был взят тест.
        Если введена дата из будущего, то вызовется ошибка.
        '''
        if dt.datetime.now().date() < data:
            raise ValidationError(
                'Это время еще не наступило!'
            )
        return data


class StatisticsSerializer(serializers.Serializer):
    '''Serializer для вывода статистики.'''
    species = serializers.CharField()
    total_tests = serializers.IntegerField()
    avg_milk_yield = serializers.FloatField()
    max_milk_yield = serializers.FloatField()
    good_health_percentage = serializers.FloatField()
