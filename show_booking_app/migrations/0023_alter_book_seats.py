# Generated by Django 5.1.7 on 2025-04-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_booking_app', '0022_book_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='seats',
            field=models.IntegerField(verbose_name=1),
        ),
    ]
