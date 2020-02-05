import math

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer

from .models import News, Contacts, Legals, Clubs, TrainingCourses, Events, Employees,ContentTypesLegals, Partners
from .serializers import AllNewsSerializers, LegalsSerializers, ContactsSerializers, AllClubsSerializers, \
    AllTrainingCoursesSerializers, AllEventsSerializers, EmployeesSerializers, ContentTypesLegalsSerializers, \
    PartnersSerializers


def paginator(model, current_page, items=2):
    first_item = (current_page - 1) * items
    last_item = current_page * items

    model_part = model[first_item:last_item]

    return model_part


def counter_years(model):
    last_event = model.first()
    first_event = model.last()

    last_year = getattr(last_event, 'date_placing').year
    first_year = getattr(first_event, 'date_placing').year

    count_years = last_year - first_year

    return count_years


# Create your views here.


class AllNewsView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        page_size = 3

        first_connection = request.GET.get('first_connection')

        current_page = int(request.GET.get('current_page'))

        all_news = News.objects.all()

        response_news = paginator(all_news, current_page, page_size)
        serializer = AllNewsSerializers(response_news, many=True)

        content = {'data': serializer.data}

        if first_connection:
            total_news = all_news.count()
            content['total_news'] = total_news
            content['page_size'] = page_size

        return Response(content)


class LegalsView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        legal_list = Legals.objects.all()
        legal_type = ContentTypesLegals.objects.filter(legals=None)

        serializer_legal = LegalsSerializers(legal_list, many=True)
        serializer_legal_type = ContentTypesLegalsSerializers(legal_type, many=True)

        content = {'legal_list': serializer_legal.data, 'legal_type_list': serializer_legal_type.data}

        return Response(content)


class ContactsView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        contacts = Contacts.objects.all()
        serializer = ContactsSerializers(contacts, many=True)
        return Response({'data': serializer.data})


class AllClubsView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        clubs = Clubs.objects.all()
        serializer = AllClubsSerializers(clubs, many=True)
        return Response({'data': serializer.data})


class AllTrainingCoursesView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        training_courses = TrainingCourses.objects.all()
        serializer = AllTrainingCoursesSerializers(training_courses, many=True)
        return Response({'data': serializer.data})


class AllEventsView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        first_connection = request.GET.get('connection')

        events = Events.objects.all()
        serializer = AllEventsSerializers(events, many=True)

        content = {'data': serializer.data}

        if first_connection:
            content['count_pages'] = counter_years(events) + 1

        return Response(content)


class EmployeesView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        employees = Employees.objects.all()
        serializer = EmployeesSerializers(employees, many=True)
        return Response({'data': serializer.data})


class PartnersView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        partners = Partners.objects.all()
        serializer = PartnersSerializers(partners, many=True)

        content = {'data': serializer.data}

        return Response(content)
