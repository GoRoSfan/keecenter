""" Serializers module

"""

from rest_framework import serializers

from .models import News, Legals, ClubType, Club, Profile


class NewsSerializers(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'title', 'post_date', 'description')


class ClubTypeSerializers(serializers.ModelSerializer):

    class Meta:
        model = ClubType
        fields = ('id', 'name')


class ClubSerializers(serializers.ModelSerializer):
    club_type = ClubTypeSerializers()

    class Meta:
        model = Club
        fields = ('id', 'name', 'description', 'club_type')


class LegalsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Legals
        fields = ('id', 'name', 'detail')


class ProfileSerializers(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'name', 'detail')


