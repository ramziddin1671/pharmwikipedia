# Generated by Django 3.2 on 2022-12-06 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmapolls', '0006_rename_file_jurnal_pdf_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='statya',
            name='language',
            field=models.CharField(choices=[('UZ', 'UZ'), ('RU', 'RU'), ('EN', 'EN')], default='UZ', max_length=2),
        ),
    ]
