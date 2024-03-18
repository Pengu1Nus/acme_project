from django.contrib import admin

from .models import Birthday


class BirthdaysAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "birthday",
        "image",
    )


admin.site.register(Birthday, BirthdaysAdmin)
