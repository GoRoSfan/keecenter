# Generated by Django 2.2.8 on 2020-02-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TrainingCourses',
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'ordering': ['id'], 'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакти'},
        ),
        migrations.AlterField(
            model_name='legals',
            name='content_type',
            field=models.ForeignKey(blank=True, on_delete=models.SET('Документ'), to='public.ContentTypesLegals', verbose_name='Тип документа'),
        ),
    ]
