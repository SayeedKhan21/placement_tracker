# Generated by Django 4.1.3 on 2023-05-06 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_company_description_company_link_company_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]
