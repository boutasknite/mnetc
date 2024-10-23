# Generated by Django 5.0.6 on 2024-06-29 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_newsevent_image_newseventparagraph'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsevent',
            name='Type',
            field=models.CharField(choices=[('option1', 'News'), ('option2', 'Event')], default='News', max_length=20),
        ),
        migrations.AddField(
            model_name='newseventparagraph',
            name='Title',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='member',
            name='Role',
            field=models.CharField(choices=[('option1', 'governance'), ('option2', 'management'), ('option2', 'member')], default='member', max_length=20),
        ),
        migrations.AlterField(
            model_name='newsevent',
            name='Title',
            field=models.CharField(default='', max_length=300),
        ),
    ]