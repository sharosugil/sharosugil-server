# Generated by Django 2.2.3 on 2019-07-24 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_auto_20190716_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='membernumber',
            field=models.CharField(default='member0', max_length=20),
        ),
    ]
