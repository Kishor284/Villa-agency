# Generated by Django 5.0.4 on 2024-05-22 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('villapp', '0015_rename_image_image1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image1',
            old_name='image',
            new_name='uimage',
        ),
    ]
