from django.contrib import admin
from .models import movies_upload,cinemas_upload,sports_upload,book

# Register your models here.

admin.site.register(movies_upload),
admin.site.register(cinemas_upload),
admin.site.register(sports_upload),
admin.site.register(book),