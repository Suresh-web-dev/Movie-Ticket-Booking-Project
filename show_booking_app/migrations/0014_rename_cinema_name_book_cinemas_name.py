# Generated by Django 5.1.7 on 2025-04-13 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show_booking_app', '0013_book_delete_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='cinema_name',
            new_name='cinemas_name',
        ),
    ]
