# Generated by Django 5.0.3 on 2024-03-28 14:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0003_remove_letter_receiver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api_app.author'),
        ),
    ]
