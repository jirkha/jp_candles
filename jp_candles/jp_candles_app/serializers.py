from rest_framework import serializers

from jp_candles_app import models

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sale
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = "__all__"


# class TransactionSerializer(serializers.ModelSerializer):
#     products = ProductSerializer(many=True)

#     class Meta:
#         model = models.Product
#         fields = ['name', 'songs']
#         extra_kwargs = {'songs': {'required': False}}

#     def create(self, validated_data):
#         songs_data = validated_data.pop('songs')
#         playlist = Playlist.objects.create(**validated_data)
#         for song_data in song_data:
#             Song.objects.create(**song_data)
#         return playlist
