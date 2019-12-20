# Generated by Django 3.0.1 on 2019-12-19 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meaning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(default='', max_length=100, verbose_name='Слово')),
                ('mean', models.CharField(default='', max_length=1000, verbose_name='Значення')),
            ],
            options={
                'verbose_name': 'Термін',
                'verbose_name_plural': 'Терміни',
            },
        ),
    ]