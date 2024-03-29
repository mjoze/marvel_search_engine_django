# Generated by Django 2.2.7 on 2019-12-11 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_m', '0002_auto_20191130_0740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'heroes',
            },
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
