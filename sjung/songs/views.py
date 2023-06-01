from django.views import generic

from . import models


class SongListView(generic.ListView):
    model = models.Song


class SongDetailView(generic.DetailView):
    model = models.Song
