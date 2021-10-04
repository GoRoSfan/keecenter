""" Serializers module

"""

from rest_framework import serializers

from .models import News, Legals, ClubType, Club, Profile


class NewsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = News
        fields = ('url', 'title', 'post_date', 'description')


class ClubTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClubType
        fields = ('name', )


class ClubSerializer(serializers.HyperlinkedModelSerializer):
    club_type = ClubTypeSerializer()

    class Meta:
        model = Club
        fields = ('url', 'name', 'description', 'club_type')


class LegalsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Legals
        fields = ('url', 'name', 'detail')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Legals
        fields = ('first_name', 'last_name', 'email')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('url', 'is_teacher', 'photo', 'user')


