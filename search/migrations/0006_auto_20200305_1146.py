# Generated by Django 3.0.1 on 2020-03-05 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20200305_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='op_food',
            name='ingredient',
            field=models.CharField(max_length=2000),
        ),
    ]