# Generated by Django 3.2.8 on 2021-11-23 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20211123_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, related_name='author_task', to='main.profile'),
        ),
        migrations.AlterField(
            model_name='task',
            name='worker',
            field=models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, related_name='worker_task', to='main.profile'),
        ),
    ]
