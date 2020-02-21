from django.db import models
from django.urls import reverse
from django import utils

# Create your models here.


class ContentTypesNews(models.Model):
    # Модель типів новин

    name = models.CharField("Назва типу новини", max_length=50)

    class Meta:
        verbose_name = 'Тип новин'
        verbose_name_plural = 'Типи новин'

    def __str__(self):
        return self.name


class News(models.Model):

    title = models.CharField("Заголовок новини", max_length=300)
    post_date = models.DateField("Дата публікації", auto_now_add=True)
    description = models.TextField("Опис новини", max_length=10000, blank=True)
    image = models.ImageField("Основне зображення новини", upload_to='image/new_image',
                              default='default/default_image_new.png')
    detail = models.FileField("Документ з детальною інформацією", upload_to='detail/new_detail/',
                              default='default/default_detail.pdf')

    VISITORS = [
        ('p', 'Батьки'),
        ('s', 'Студенти'),
        ('w', 'Працівники'),
        ('f', 'Партнери'),
    ]

    visitors_type = models.CharField("Тип користувача", max_length=1, choices=VISITORS, default='s')

    content_types = models.ManyToManyField(ContentTypesNews, default='Загальний', verbose_name='Типи новини',
                                           related_name='news')

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'

        ordering = ['-id']

    def display_content_types(self):
        return ', '.join([content_type.name for content_type in self.content_types.all()[:3]])

    display_content_types.short_description = 'Типи новини'

    def __str__(self):
        return '{0} - {1}'.format(self.title, self.post_date)

    def get_absolute_url(self):
        return reverse('new-detail', args=[str(self.id)])


class Events(models.Model):

    name = models.CharField("Назва події", max_length=150)
    date_placing = models.DateTimeField("Дата проходження події", default=utils.timezone.now)
    detail = models.FileField("Документ з детальною інформацією", upload_to='detail/event_detail/',
                              default='default/default_detail.pdf')

    class Meta:
        verbose_name = 'Подія'
        verbose_name_plural = 'Події'

        ordering = ['-date_placing']

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.date_placing)

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])


class ActivityTypesClubs(models.Model):
    # Модель типів діяльності гуртків

    name = models.CharField("Назва типу гуртка", max_length=50)

    class Meta:
        verbose_name = 'Тип діяльності гуртків'
        verbose_name_plural = 'Типи діяльності гуртків'

    def __str__(self):
        return self.name


class Clubs(models.Model):

    name = models.CharField("Назва гуртка", max_length=150)
    description = models.TextField("Опис діяльності гуртка", max_length=5000,
                                   help_text="Введіть основну інформацію про гурток", blank=True)
    image = models.ImageField("Емблема або інше характерне зображення", upload_to='image/club_image/',
                              default='default/default_image_club.png')
    detail = models.FileField("Документ з детальою інформацією", upload_to='detail/club_detail/',
                              default='default/default_detail.pdf')

    SEASONS = [
        ('a', 'Весь рік'),
        ('e', 'Академічний рік'),
        ('s', 'Літні канікули'),
    ]

    season_set = models.CharField("Час активності", max_length=1, choices=SEASONS)

    AGE = [
        ('p', 'Учні'),
        ('s', 'Студенти'),
        ('c', 'Учні/Студенти'),
    ]

    members_age = models.CharField("Вік відвідувачів гуртка", max_length=1, choices=AGE, default='c')

    activity_type = models.ForeignKey(ActivityTypesClubs, on_delete=models.SET('Навчальний'),
                                      verbose_name='Напрямок діяльності гуртка')

    class Meta:
        verbose_name = 'Гурток'
        verbose_name_plural = 'Гуртки'

        ordering = ['name']

    def __str__(self):
        return 'Гурток - {0} - {1}({2}). Діє {3}'.format(self.name, self.activity_type, self.members_age,
                                                         self.season_set)

    def get_absolute_url(self):
        return reverse('club-detail', args=[str(self.id)])


class Contacts(models.Model):

    label = models.CharField("Назва кантакту", max_length=50)
    content = models.CharField("Зміст контакту", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакти'

        ordering = ['id']

    def __str__(self):
        return '{0}: {1}'.format(self.label, self.content)


class ContentTypesLegals(models.Model):
    # Модель типів документів

    name = models.CharField("Назва типу документа", max_length=50)

    class Meta:
        verbose_name = 'Тип документів'
        verbose_name_plural = 'Типи документів'

    def __str__(self):
        return self.name


class Legals(models.Model):

    name = models.CharField("Назва документа", max_length=100)
    detail = models.FileField("Документ з детальою інформацією", upload_to='detail/legal_detail/',
                              default='default/default_detail.pdf')
    content_type = models.ForeignKey(ContentTypesLegals, on_delete=models.SET('Документ'),
                                     verbose_name='Тип документа', blank=True)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документи'

        ordering = ['name']

    def __str__(self):
        return self.name


class Employees(models.Model):

    first_name = models.CharField("Им'я", max_length=25)
    last_name = models.CharField("Прізвище", max_length=40)
    position = models.CharField("Посада", max_length=35)

    characters = models.TextField("Характеристика", max_length=1000, help_text="")

    photo = models.ImageField("Фотокартка", upload_to='image/employee_image/',
                              default='default/default_image_employee.png')

    class Meta:
        verbose_name = 'Співробітник'
        verbose_name_plural = 'Співробітники'

        ordering = ['last_name', 'first_name']

    def __str__(self):
        return '{0}, {1}'.format(self.first_name, self.last_name)


class Partners(models.Model):

    title = models.CharField("Назва організації", max_length=100)
    description = models.TextField("Короткий опис", max_length=1000)

    partner_link = models.URLField("Посилання на сайт партнера", max_length=100)

    logo = models.ImageField("Логотип", upload_to='image/partner_image/',
                             default='default/default_image_partner.png')

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнери'

        ordering = ['title']

    def __str__(self):
        return self.title

