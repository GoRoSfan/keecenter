from django.test import TestCase

from public.models import News, ContentTypesNews, ContentTypesLegals, ActivityTypesClubs


class TestModelContentTypesNews(TestCase):

    @classmethod
    def setUpTestData(cls):
        ContentTypesNews.objects.create(name='Дослідницькі роботи')
        print("egergegqe gerger rgsdfg regsdfhe")

    def test_object_name_is_name_of_type(self):
        type_news = ContentTypesNews.objects.get(id=1)
        object_name = type_news.name

        self.assertEqual(object_name, 'Дослідницькі роботи')


class TestModelActivityTypesClubs(TestCase):

    @classmethod
    def setUpTestData(cls):
        ActivityTypesClubs.objects.create(name='Фізика')

    def test_object_name_is_name_of_type(self):
        type_contact = ActivityTypesClubs.objects.get(id=1)
        object_name = type_contact.name

        self.assertEqual(object_name, str(type_contact))


class TestModelTypesLegals(TestCase):

    @classmethod
    def setUpTestData(cls):
        ContentTypesLegals.objects.create(name='Правові')

    def test_object_name_is_name_of_type(self):
        type_legals = ContentTypesLegals.objects.get(id=1)
        object_name = type_legals.name

        self.assertEqual(object_name, str(type_legals))


class TestModelNews(TestCase):

    @classmethod
    def setUpTestData(cls):
        ContentTypesNews.objects.create(name='Дослідницькі роботи')
        News.objects.create(title='Роботи-боботи', description='bla-bla', visitors_type='p')
        News.objects.get(id=1).save()
        first = News.objects.get(id=1)
        first.content_types.add(ContentTypesNews.objects.get(id=1))

    def test_image_default(self):
        new = News.objects.get(id=1)
        default_image = new._meta.get_field('image').default

        self.assertEqual(default_image, 'default/default_image_new.png')
