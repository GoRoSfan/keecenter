""" Serializers module

"""

from rest_framework import serializers

from .models import NewContentTypes, News, LegalContentTypes, Legals, \
    Contacts, Events, Employees, Partners


class FileUrlField(serializers.Field):
    """ FileUrlField

    """


class NewContentTypesSerializers(serializers.ModelSerializer):
    """ NewContentTypes serializer

    """

    class Meta:
        model = NewContentTypes
        fields = ('id', 'name')


class AllNewsSerializers(serializers.ModelSerializer):
    """ AllNews serializer

    """

    content_types = NewContentTypesSerializers(many=True)
    image_url = FileUrlField(source='image_hash')

    class Meta:
        model = News
        fields = ('id', 'title', 'post_date', 'description', 'image_url', 'image',
                  'detail', 'visitors_type', 'content_types')


class LegalContentTypesSerializers(serializers.ModelSerializer):
    """ LegalContentTypes serializer

    """

    class Meta:
        model = LegalContentTypes
        fields = ('id', 'name')


class LegalsSerializers(serializers.ModelSerializer):
    """ Legals serializer

    """

    content_type = LegalContentTypesSerializers()

    class Meta:
        model = Legals
        fields = ('id', 'name', 'detail')


class ContactsSerializers(serializers.ModelSerializer):
    """ Contacts serializer

    """

    class Meta:
        model = Contacts
        fields = ('id', 'label', 'content')


class AllEventsSerializers(serializers.ModelSerializer):
    """ AllEvents serializer

    """

    class Meta:
        model = Events
        fields = ('id', 'name', 'date_placing', 'detail')


class EmployeesSerializers(serializers.ModelSerializer):
    """ Employees serializer

    """

    class Meta:
        model = Employees
        fields = ('id', 'first_name', 'last_name', 'position', 'characters', 'photo')


class PartnersSerializers(serializers.ModelSerializer):
    """ Partners serializer

    """

    class Meta:
        model = Partners
        fields = ('id', 'title', 'description', 'partner_link', 'logo')
