# Generated by Django 5.0.6 on 2024-06-15 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_application_biography_application_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='Image',
            field=models.ImageField(default='Members_Photos/default.jpg', upload_to='Members_Photos/'),
        ),
    ]
