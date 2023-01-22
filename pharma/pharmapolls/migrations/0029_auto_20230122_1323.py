# Generated by Django 3.2 on 2023-01-22 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmapolls', '0028_auto_20230122_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='button_en',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='button_ru',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='button_uz',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='subtitle_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='subtitle_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='subtitle_uz',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='title_uz',
            field=models.CharField(max_length=200, null=True),
        ),
    ]