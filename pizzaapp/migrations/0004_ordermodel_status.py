# Generated by Django 3.0.2 on 2020-07-13 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0003_ordermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(default=False, max_length=10),
        ),
    ]
