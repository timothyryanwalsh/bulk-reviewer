# Generated by Django 2.0.9 on 2018-11-17 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_namedentity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='namedentity',
            old_name='name_type',
            new_name='label',
        ),
    ]