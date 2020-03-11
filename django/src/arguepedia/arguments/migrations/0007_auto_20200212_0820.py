# Generated by Django 3.0.2 on 2020-02-12 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arguments', '0006_auto_20200212_0756'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='argumentpost',
            options={'ordering': ['-updated', 'timestamp']},
        ),
        migrations.RemoveField(
            model_name='argumentpost',
            name='content',
        ),
        migrations.RemoveField(
            model_name='argumentpost',
            name='publish_date',
        ),
        migrations.RemoveField(
            model_name='argumentpost',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='argumentpost',
            name='title',
        ),
        migrations.AlterField(
            model_name='action',
            name='explanation',
            field=models.TextField(max_length=220),
        ),
    ]
