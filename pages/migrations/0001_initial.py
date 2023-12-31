# Generated by Django 4.2.4 on 2023-08-31 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='serachArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlesearceh', models.CharField(max_length=75, verbose_name='title-search')),
                ('title', models.CharField(max_length=75, verbose_name='title')),
                ('description', models.TextField(max_length=175, verbose_name='description')),
                ('url', models.URLField(max_length=27, verbose_name='URL')),
                ('status', models.BooleanField(default=False, verbose_name='STATUS')),
            ],
        ),
    ]
