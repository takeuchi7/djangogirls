# Generated by Django 2.0.6 on 2019-05-03 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190503_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='number',
            field=models.CharField(max_length=200, null=True),
        ),
    ]