from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer для просмотра и создания записей для Продуктов."""
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price'
        )

    def validate_name(self, value):
        """Проверка корректности поля name."""
        if not value.strip():
            raise serializers.ValidationError(
                "Название не может быть пустым."
            )
        return value

    def validate_description(self, value):
        """Проверка корректности поля description."""
        if len(value) > 100:
            raise serializers.ValidationError(
                "Описание не должно превышать 100 символов."
            )
        return value

    def validate_price(self, value):
        """Проверка корректности поля price."""
        if value <= 0:
            raise serializers.ValidationError(
                "Цена должна быть положительным числом."
            )
        return value
