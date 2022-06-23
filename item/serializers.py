from rest_framework import serializers
from item.models import Category as CategoryModel
from item.models import Item as ItemModel
from item.models import Order as OrderModel
from item.models import ItemOrder as ItemOrderModel


# 1. CategorySerializer 구현
class CategorySerializer(serializers.ModelSerializer):
    model: CategoryModel
    fields = ["name"]

# 2. ItemSerializer 구현
class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    model: ItemModel
    fields = ["name", "category", "image_url"]

# 3. OrderSerializer 구현
class OrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True)
    model: OrderModel
    fields = ["delivery_address", "order_date", "item", ]

# 4. ItemOrderSerializer 구현
class ItemOrderSerializer(serializers.ModelSerializer):
    order = OrderSerializer(many=True)
    model: ItemOrderModel
    fields = ["order", "item", "item_count", ]


