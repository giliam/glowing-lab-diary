# Generated by Django 3.0.3 on 2020-03-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_auto_20200303_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusentry',
            name='css_class',
            field=models.CharField(default='btn-primary', max_length=150),
        ),
        migrations.AddField(
            model_name='statusentry',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
