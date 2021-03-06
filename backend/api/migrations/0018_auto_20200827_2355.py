# Generated by Django 3.1 on 2020-08-27 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20200827_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='credits',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='course',
            name='credits_required',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]
