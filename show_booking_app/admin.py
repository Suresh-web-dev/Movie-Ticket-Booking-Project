from django.contrib import admin
from .models import sign,log,image_upload,events_upload,sports_upload,cinemas_upload,book

# Register your models here.

admin.site.register(sign),
admin.site.register(log),
admin.site.register(image_upload),
admin.site.register(events_upload),
admin.site.register(sports_upload),
admin.site.register(cinemas_upload),
admin.site.register(book),

