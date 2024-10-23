# Generated by Django 5.0.6 on 2024-07-02 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_newsevent_date_newsevent_place_alter_member_role_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication_Elearning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(choices=[('E-learning', 'E-learning'), ('Publication', 'Publication')], default='E-learning', max_length=20)),
                ('Title', models.CharField(default='', max_length=300)),
                ('Date', models.DateField()),
                ('File', models.FileField(upload_to='Publication_Elearning/')),
            ],
        ),
        migrations.CreateModel(
            name='Seminars_Webinars_Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(choices=[('Seminars & Webinars', 'Seminars & Webinars'), ('Podcast', 'Podcast')], default='Seminars & Webinars', max_length=20)),
                ('Title', models.CharField(default='', max_length=300)),
                ('Date', models.DateField()),
                ('Link', models.CharField(max_length=500)),
            ],
        ),
    ]