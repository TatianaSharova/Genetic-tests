import datetime as dt

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from .constans import MAX_LENGTH, MAX_LENGTH_STATUS, MIN_NUM, STATUSES


class Test(models.Model):
    '''Модель для генетических тестов.'''
    animal_name = models.CharField(max_length=MAX_LENGTH)
    species = models.CharField(max_length=MAX_LENGTH)
    test_date = models.DateField()
    milk_yield = models.FloatField(validators=[
            MinValueValidator(
                MIN_NUM, f'Минимальное значение {MIN_NUM}.'),
        ],)
    health_status = models.CharField(choices=STATUSES,
                                     max_length=MAX_LENGTH_STATUS)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.animal_name}'

    def validate(self, test_date):
        if dt.datetime.now().date() < test_date:
            raise ValidationError(
                'Это время еще не наступило!'
            )
