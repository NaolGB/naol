# Generated by Django 4.0 on 2022-11-03 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_experience_experence_end_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Certification',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
