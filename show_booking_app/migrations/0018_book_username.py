# Generated by Django 5.1.7 on 2025-04-17 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_booking_app', '0017_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
