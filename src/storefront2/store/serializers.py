

from decimal import Decimal

from rest_framework import serializers
from store.models import Collection, Product, Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'name', 'date', 'description')

    def create(self, validated_data):

        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)


class CollectionSerializer(serializers.Serializer):

    class Meta:

        model = Collection
        fields = ('id', 'title', 'products_count')

    products_count = serializers.IntegerField()



class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = ('id', 'title', 'description', 'slug', 'inventory', 'unit_price', 'collection', 'price_with_tax')


    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product: Product) -> Decimal:
        return product.unit_price * Decimal(1.1)


    # def validate(self, data): ...

    # def create(self, validated_data):

    #     product = Product(**validated_data)
    #     product.other_field = 1
    #     product.save()

    #     return product

    # def update(self, instance, validated_data):
    #     instance.unit_price = validated_data.get('unit_price')
    #     instance.save()
    #     return instance


# class ProductSerializer(serializers.Serializer):

#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
#     price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
#     # collection = serializers.PrimaryKeyRelatedField(
#     #     queryset=Collection.objects.all(),
#     # )

#     # collection = serializers.StringRelatedField()

#     # collection = CollectionSerializer()

#     collection = serializers.HyperlinkedRelatedField(
#         queryset=Collection.objects.all(),
#         view_name='collection-detail'
#     )

#     def calculate_tax(self, product: Product) -> Decimal:
#         return product.unit_price * Decimal(1.1)
