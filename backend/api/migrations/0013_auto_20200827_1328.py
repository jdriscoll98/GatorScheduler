# Generated by Django 3.1 on 2020-08-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_semester_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plannedcourse',
            name='term',
        ),
        migrations.AlterField(
            model_name='semester',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]