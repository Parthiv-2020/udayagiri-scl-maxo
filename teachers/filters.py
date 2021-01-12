import django_filters
from django_filters import CharFilter
from .models import Teacher


class TeacherFilter(django_filters.FilterSet):
    description = CharFilter(field_name='description', lookup_expr='icontains')
    teaching_experience_gt = django_filters.NumberFilter(field_name='teaching_experience', lookup_expr='gt')
    class Meta:
        model = Teacher
        fields = ['subject', 'country']