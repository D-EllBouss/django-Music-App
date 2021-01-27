from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/album_id/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/songs/
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),

    # /music/songs_id/favorite/
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

    # /music/create album/
    url(r'^create_album/$', views.create_album, name='create_album'),

    # /music/album_id/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),

    # /music/album/album_id/update/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='update_album'),

    # /music/album_id/create_song/
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),

    # /music/album_id/delete_song/
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),

    # /music/album/album_id/delete/
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),


]
