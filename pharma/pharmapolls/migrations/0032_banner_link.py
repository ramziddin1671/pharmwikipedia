# Generated by Django 4.1.5 on 2023-01-30 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmapolls', '0031_auto_20230122_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='link',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]