import random
import string

import pytest
from django.urls import reverse

import sjung.songs.models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_song(**kwargs):
    defaults = {}
    defaults["text"] = random_string(100)
    defaults["source"] = random_string(5)
    defaults["notes"] = random_string(5)
    defaults["melody"] = random_string(5)
    defaults["title"] = random_string(10)
    defaults["slug"] = random_string(5)
    defaults["text_author"] = random_string(5)
    defaults.update(**kwargs)
    return sjung.songs.models.Song.objects.create(**defaults)


pytestmark = [pytest.mark.django_db]


def tests_song_list_view(client):
    instance1 = create_song()
    instance2 = create_song()
    url = reverse("Song_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_song_detail_view(client):
    instance = create_song()
    url = reverse(
        "Song_detail",
        args=[
            instance.slug,
        ],
    )
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")
