# Generated by Django 5.0.6 on 2024-06-15 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_application_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='User_Id',
            field=models.IntegerField(default=2),
        ),
    ]
