# Generated by Django 3.2.4 on 2021-07-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('Corporate Headoffice', 'Corporate Headoffice'), ('Operations Department', 'Operations Department'), ('Work Station', 'Work Station'), ('Marketing Division', 'Marketing Division')], default='Corporate Headoffice', max_length=50)),
                ('department', models.TextField(max_length=500)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('incidentlocation', models.TextField(max_length=500)),
                ('saverity', models.CharField(choices=[('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Severe', 'Severe'), ('Fatal', 'Fatal')], default='Mild', max_length=50)),
                ('cause', models.TextField(max_length=500)),
                ('actiontaken', models.TextField(max_length=500)),
            ],
        ),
    ]