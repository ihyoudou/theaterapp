# Generated by Django 3.2.12 on 2022-03-21 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0002_auto_20220321_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='itemID',
            new_name='item',
        ),
    ]