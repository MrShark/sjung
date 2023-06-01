from django import forms
from django.contrib import admin

from . import models


class SongAdminForm(forms.ModelForm):
    class Meta:
        model = models.Song
        fields = "__all__"


class SongAdmin(admin.ModelAdmin):
    form = SongAdminForm
    prepopulated_fields = {"slug": ["title"]}
    list_display = [
        "last_updated",
        "title",
        "text_author",
        "created",
        "melody",
        "source",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


admin.site.register(models.Song, SongAdmin)
