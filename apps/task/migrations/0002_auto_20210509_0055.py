# Generated by Django 3.2 on 2021-05-08 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskassignee',
            name='task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='task.task'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taskassignee',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.user'),
            preserve_default=False,
        ),
    ]
