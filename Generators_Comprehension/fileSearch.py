import os
import fnmatch


def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        for artist in fnmatch.filter(directories, artist_name):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):   # album[0] to get only path of the album
            yield song


albums_list = find_albums('music', 'aerosmith')
songs_list = find_songs(albums_list)
for s in songs_list:
    print(s)
