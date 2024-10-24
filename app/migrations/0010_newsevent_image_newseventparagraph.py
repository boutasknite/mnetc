# Generated by Django 5.0.6 on 2024-06-29 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_newsevent_alter_member_image_newseventimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsevent',
            name='Image',
            field=models.ImageField(default='Members_Photos/default.jpg', upload_to='NewsEvent/'),
        ),
        migrations.CreateModel(
            name='NewsEventParagraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Paragraph', models.TextField(default='')),
                ('NewsEvent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraphs', to='app.newsevent')),
            ],
        ),
    ]
