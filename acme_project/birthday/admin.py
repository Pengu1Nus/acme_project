from django.contrib import admin

from .models import Birthday, Tag


class BirthdaysAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "birthday",
        "image",
    )


class TagsAdmin(admin.ModelAdmin):
    list_display = ("tag",)


admin.site.register(Birthday, BirthdaysAdmin)
admin.site.register(Tag, TagsAdmin)
