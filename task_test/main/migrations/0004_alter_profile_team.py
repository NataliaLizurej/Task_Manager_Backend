# Generated by Django 3.2.8 on 2021-10-27 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211027_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='team',
            field=models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, to='main.team'),
        ),
    ]
