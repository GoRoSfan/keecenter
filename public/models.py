""" Models module

"""

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class News(models.Model):

    title = models.CharField("Заголовок новини", max_length=300)
    post_date = models.DateField("Дата публікації", auto_now_add=True)
    description = models.TextField("Опис новини", max_length=10000, blank=True)

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
        ordering = ['-id']

    def __str__(self):
        return '{0} - {1}'.format(self.title, self.post_date)

    def get_absolute_url(self):
        return reverse('new-detail', args=[str(self.id)])


class ClubType(models.Model):

    name = models.CharField("Назва типу гуртка", max_length=50)

    class Meta:
        verbose_name = 'Тип гуртків'
        verbose_name_plural = 'Типи гуртків'

    def __str__(self):
        return self.name


class Club(models.Model):

    name = models.CharField("Назва гуртка", max_length=150)
    description = models.TextField(
        "Опис діяльності гуртка", max_length=5000, blank=True,
        help_text="Введіть основну інформацію про гурток")
    club_type = models.ForeignKey(
        ClubType, on_delete=models.SET('Навчальний'),
        verbose_name='Тип гуртка'
    )

    class Meta:
        verbose_name = 'Гурток'
        verbose_name_plural = 'Гуртки'
        ordering = ['name']

    def __str__(self):
        return 'Гурток: {0} - {1}' \
               ''.format(self.name, self.club_type)

    def get_absolute_url(self):
        return reverse('club-detail', args=[str(self.id)])


class Legals(models.Model):

    name = models.CharField("Назва документа", max_length=100)
    detail = models.FileField(
        "Документ з детальою інформацією", upload_to='detail/legal_detail/',
        default='default/default_detail.pdf')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документи'
        ordering = ['name']

    def __str__(self):
        return self.name


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField("Им'я", max_length=25)
    last_name = models.CharField("Прізвище", max_length=40)
    is_teacher = models.BooleanField('Вчитель', max_length=35, default=False)
    photo = models.ImageField("Фотокартка", upload_to='image/employee_image/',
                              default='default/default_image_employee.png')

    class Meta:
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профелі'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return '{0}, {1}'.format(self.first_name, self.last_name)
