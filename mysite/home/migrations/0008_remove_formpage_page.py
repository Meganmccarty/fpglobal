# Generated by Django 3.0.7 on 2020-06-25 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_formpage_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formpage',
            name='page',
        ),
    ]
