# Generated by Django 5.1.1 on 2024-09-25 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField(max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
