# Generated by Django 3.2 on 2022-12-03 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmapolls', '0005_jurnal_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jurnal',
            old_name='file',
            new_name='pdf_file',
        ),
    ]
