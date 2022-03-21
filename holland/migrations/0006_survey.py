# Generated by Django 3.2 on 2022-03-21 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holland', '0005_alter_crop_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(max_length=20)),
                ('name', models.TextField(max_length=20)),
                ('namep', models.TextField(max_length=20)),
                ('regd', models.IntegerField()),
                ('number', models.IntegerField()),
                ('system', models.TextField(max_length=20)),
                ('spacing', models.TextField(max_length=20)),
                ('crop', models.TextField(max_length=20)),
                ('pump', models.TextField(max_length=20)),
                ('area', models.TextField(max_length=20)),
                ('type', models.TextField(max_length=20)),
            ],
        ),
    ]