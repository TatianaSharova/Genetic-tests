from django.urls import include, path
from rest_framework.routers import DefaultRouter as Router

from .views import StatisticsView, TestViewSet

router_v1 = Router()
router_v1.register('tests', TestViewSet, basename='test')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('statistics/', StatisticsView.as_view(), name='read_statistics')
]
