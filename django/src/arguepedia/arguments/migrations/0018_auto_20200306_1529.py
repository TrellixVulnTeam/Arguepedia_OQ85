# Generated by Django 3.0.2 on 2020-03-06 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arguments', '0017_auto_20200305_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='argumentpost',
            name='initial',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='InitialArgument',
        ),
    ]
