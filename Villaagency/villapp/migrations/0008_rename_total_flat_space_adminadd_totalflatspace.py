# Generated by Django 5.0.4 on 2024-05-15 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('villapp', '0007_adminadd_delete_adminadd11'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminadd',
            old_name='total_flat_space',
            new_name='totalflatspace',
        ),
    ]
