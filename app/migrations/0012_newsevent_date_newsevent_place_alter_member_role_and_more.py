# Generated by Django 5.0.6 on 2024-06-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_newsevent_type_newseventparagraph_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsevent',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='newsevent',
            name='Place',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='Role',
            field=models.CharField(choices=[('governance', 'governance'), ('management', 'management'), ('member', 'member')], default='member', max_length=20),
        ),
        migrations.AlterField(
            model_name='newsevent',
            name='Type',
            field=models.CharField(choices=[('News', 'News'), ('Event', 'Event')], default='News', max_length=20),
        ),
    ]