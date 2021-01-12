import django_filters
from django_filters import CharFilter
from .models import Teacher


class TeacherFilter(django_filters.FilterSet):
    description = CharFilter(field_name='description', lookup_expr='icontains')
    age__gt = django_filters.NumberFilter(field_name='age', lookup_expr='gt')
    age__lt = django_filters.NumberFilter(field_name='age', lookup_expr='lt')
    class Meta:
        model = Teacher
        fields = ['subject', 'country']