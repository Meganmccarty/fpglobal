# Generated by Django 3.0.7 on 2020-06-23 16:13

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='expertise_title',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro_body',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro_title',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='NewsPageGalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('expertise_item', models.CharField(blank=True, max_length=250)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='expertise_items', to='home.HomePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
