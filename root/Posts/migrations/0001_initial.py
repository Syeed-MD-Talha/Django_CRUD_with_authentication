# Generated by Django 5.0.6 on 2024-06-07 17:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('published_date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'posts',
                'ordering': ['-published_date'],
            },
        ),
    ]
