# Generated by Django 5.0.3 on 2024-03-28 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0004_alter_letter_sender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='letter',
            name='receiver',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_app.user'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='sender',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='api_app.author'),
        ),
        migrations.AddField(
            model_name='letter',
            name='tag',
            field=models.ManyToManyField(to='api_app.tag'),
        ),
    ]