from django.db import models
from django.urls import reverse


class Song(models.Model):
    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    text = models.TextField()
    text_author = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    notes = models.TextField(blank=True)
    melody = models.CharField(max_length=100, blank=True)
    source = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "song"
        verbose_name_plural = "songs"

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("Song_detail", args=(self.slug,))
