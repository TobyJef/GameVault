# Generated by Django 3.2.25 on 2024-09-30 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20240927_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='category',
        ),
        migrations.DeleteModel(
            name='Console',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
    ]