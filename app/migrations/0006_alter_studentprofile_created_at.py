# Generated by Django 4.1.3 on 2023-05-06 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_studentprofile_created_at_studentprofile_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
