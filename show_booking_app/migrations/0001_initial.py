# Generated by Django 5.1.7 on 2025-04-05 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('password1', models.CharField(max_length=255, null=True)),
                ('password2', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
