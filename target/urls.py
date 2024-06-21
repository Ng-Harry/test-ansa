from django.urls import path
from . import views

urlpatterns = [
    path('user-billboard-stats/monthly-stats', views.MonthlyTarget.as_view(), name='monthly-stats'),
]
