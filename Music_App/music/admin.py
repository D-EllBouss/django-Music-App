from django.contrib import admin
from .models import Album, Song


# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    list_display = ("album_title", "artist", "is_favorite", "user")
    list_filter = ("genre", "artist", "is_favorite")
    search_fields = ("album_title", "artist", "genre")


class SongAdmin(admin.ModelAdmin):
    list_display = ("song_title", "album", "is_favorite")
    list_filter = ("album", "is_favorite")
    search_fields = ("song_title",)


admin.site.register(Song, SongAdmin)

admin.site.register(Album, AlbumAdmin)

