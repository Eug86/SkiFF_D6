import django_filters
from django_filters import FilterSet, ModelChoiceFilter
from .models import Category
from django.forms import DateTimeInput


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Title',
    )
    dateCreation = django_filters.DateTimeFilter(
        field_name='time_in',
        lookup_expr='gt',
        label='Date',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )


    category = django_filters.ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Category',
        empty_label='Select a category',
    )
