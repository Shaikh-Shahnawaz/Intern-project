# Generated by Django 3.2.4 on 2021-07-17 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myintern', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='enviromentalincident',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='report',
            name='injuryillness',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='report',
            name='propertydamage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='report',
            name='vehicle',
            field=models.BooleanField(default=False),
        ),
    ]