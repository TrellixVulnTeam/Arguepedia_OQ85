# Generated by Django 3.0.2 on 2020-02-06 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arguments', '0009_argumentpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='argumentpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
