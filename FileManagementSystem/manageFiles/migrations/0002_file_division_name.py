# Generated by Django 4.0.4 on 2022-05-30 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageFiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='division_name',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
