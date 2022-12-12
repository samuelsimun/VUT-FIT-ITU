# Generated by Django 4.1.2 on 2022-12-13 21:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projet_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('final_deadline', models.DateField(default=django.utils.timezone.now)),
                ('deadlines', models.TextField(null=True)),
                ('team', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
