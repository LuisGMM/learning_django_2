
from django_filters import filterset

from .models import Product


class ProductFilterSet(filterset.FilterSet):

    class Meta:
        model = Product
        fields = {
            'collection_id': ['exact'],
            'unit_price': ['gt', 'lt']
        }
