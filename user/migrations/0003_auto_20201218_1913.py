# Generated by Django 3.1.3 on 2020-12-18 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201216_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.ImageField(default='default.png', null=True, upload_to=''),
        ),
    ]