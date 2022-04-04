from django.shortcuts import render
from .models import singer
from django.views.generic.list import ListView
import django_filters


class SingerFilter(django_filters.FilterSet):
    '''
        Custom filter for filtering singer by name, country_code etc.
        ip_address:?name=John
    '''
    class Meta:
        model = singer
        fields = ["name", "country_code", "date_of_birth",
            "stage_name__stage_name", "extra_param__extra_param"]


class SingerList(ListView):
    '''
        Listing singers data
    '''
    model = singer

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = SingerFilter(self.request.GET, queryset)
        return filter.qs
