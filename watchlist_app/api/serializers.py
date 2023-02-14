from rest_framework import serializers
from ..models import Movies

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movies.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
