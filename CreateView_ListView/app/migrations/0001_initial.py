# Generated by Django 5.0.2 on 2024-04-10 18:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('sname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('sprincipal', models.CharField(max_length=50)),
                ('scontact', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdname', models.CharField(max_length=50)),
                ('stdage', models.IntegerField()),
                ('sname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.school')),
            ],
        ),
    ]
