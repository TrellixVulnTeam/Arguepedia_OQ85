# Generated by Django 3.0.2 on 2020-02-12 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arguments', '0004_auto_20200212_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='argument_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arguments.ArgumentPost'),
        ),
    ]
