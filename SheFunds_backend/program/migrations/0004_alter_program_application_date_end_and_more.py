# Generated by Django 4.2.6 on 2023-10-11 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0003_applicant_home_city_applicant_pronouns_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='application_date_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='program',
            name='application_date_start',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='program',
            name='date_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='program',
            name='date_start',
            field=models.DateField(),
        ),
    ]
