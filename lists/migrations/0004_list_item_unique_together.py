# Generated by Django 3.0.5 on 2020-04-13 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20200321_2037'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('list', 'text')},
        ),
    ]
