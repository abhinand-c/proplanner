# Generated by Django 3.2 on 2021-05-08 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='role_level',
            field=models.IntegerField(choices=[(0, 'Junior'), (1, 'Mid'), (2, 'Senior')], default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='interests',
            field=models.ManyToManyField(blank=True, related_name='skill_interests', to='core.Skill'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.role'),
        ),
        migrations.AddField(
            model_name='user',
            name='skills',
            field=models.ManyToManyField(blank=True, to='core.Skill'),
        ),
    ]
