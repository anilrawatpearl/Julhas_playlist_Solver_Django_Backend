# Generated by Django 2.2 on 2019-04-29 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='categories',
            field=models.CharField(max_length=50),
        ),
    ]