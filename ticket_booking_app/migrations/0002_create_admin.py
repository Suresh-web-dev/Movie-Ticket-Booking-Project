from django.db import migrations

def create_admin(apps, schema_editor):
    User = apps.get_model("auth", "User")
    if not User.objects.filter(username="Whereismyseat").exists():
        User.objects.create_superuser(
            username="Whereismyseat",
            email="dssuresh68@gmain.com",
            password="myproject"
        )

class Migration(migrations.Migration):

    dependencies = [
        ("ticket_booking_app", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_admin),
    ]
