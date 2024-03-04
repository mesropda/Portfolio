import django_filters
from .models import Transactions
from django import forms


class TransactionFilter(django_filters.FilterSet):
    amount = django_filters.RangeFilter()
    date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Transactions
        fields = {
            'transaction_type': ['exact'],
            # 'amount': ['lt', 'gt'],
            'category': ['exact'],
            'source': ['exact'],
            # 'date': ['exact', 'range']
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.filters['amount'].widget.attrs.update(
    #         {'class': 'form_input_register'})
