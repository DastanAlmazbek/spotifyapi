from dataclasses import field
from rest_framework import serializers
from .models import Song, SongReview, SongFavorite


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','title', 'genre', 'year', 'author', 'image')
        model = Song



class SongReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = SongReview
        fields = "__all__"

    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValidationError(
                "Рейтинг должен быть от 1 до 5"
            )
        return rating

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["user"] = instance.user.email
        representation["song"] = instance.song.title
        return representation    
     

class SongFavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = SongFavorite
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["user"] = instance.user.email
        representation["song"] = instance.song.title
        return representation