class Song:
    """This is class to represent a song

    Attributes:
        title: The title of the song.
        artist: The name of the song creator
        duration: Duration of the song in secs.
            Will default to zero if not specified.
    """

    def __init__(self, title: str, artist: str, duration: int = 0):
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_name(self):
        return self.title

    name = property(get_name)


class Album:
    """class to represent album using track's list
    Attributes:
        name: the name of the album
        year: the year in which the album was released
        artist: Name of the artist responsible for the album. If
            not specified will default to name 'various artist'.
        tracks: list of the song for the current album

    Methods:
        add_song: this will add song to the album's tracks list
    """

    def __init__(self, name: str, year: int, artist: str = None):
        """Initialises class `Album` """

        self.name = name
        self.year = year
        if artist:
            self.artist = artist
        else:
            self.artist = 'various artist'
        self.tracks = []

    def add_song(self, song: str, position: int = 0):
        """adds song to the track list
            Args:
                song: song object to be added to track list
                position(int): position on which the song should be added on
                    (If specified). Otherwise, it will be added on the
                    end of the list.
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position:
                self.tracks.insert(position, song_found)
            else:
                self.tracks.append(song_found)


class Artist:
    """"Basic class to store artist details

    Attributes:
        name: Name of the artist
        albums(List[Album]): list of albums responsible for the artist. The
            list only shows album in this collection.

    Methods:
        add_album: used to add album to the collection (artist's album list)
    """

    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        """Add album to the artist's album list.
            :param album: album object to be added to the list.
                if the album already exist won't be added again (yet to
                be implemented).
        """

        self.albums.append(album)

    def add_song(self, name: str, year: int, title: str):
        """this method will add the song to the collection of albums.
        A new album will be created if it does not already exist in the
        collection.
        :param name: the name of the album in the collection
        :param year: the year the album was produced (released)
        :param title: The song title
        """

        album_found = find_object(name, self.albums)
        if album_found is None:
            print(f"{name} not found")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print(f"{name} found")
        album_found.add_song(title)


def find_object(element, check_list: list):
    """Check if the passed field ` exist in a list `check_list` or not.
    :param element: element to check if exist in the given list.
    :param check_list: list to check from.
    :return: The function will return none if the element exist in a list,
        else the element it's self.
    """

    for obj in check_list:
        if obj.name == element:
            return obj
    return None


def load_data():
    """The function will load data from file to appropriate places"""
    file_name = "albums.txt"
    artist_list = []
    with open(file_name, 'r', encoding='utf-8') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(
                line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)

            current_artist = find_object(artist_field, artist_list)
            if current_artist is None:
                current_artist = Artist(artist_field)
                artist_list.append(current_artist)
            current_artist.add_song(album_field, year_field, song_field)

    return artist_list


def creating_check_file(artists_list):
    """creating check file from the object data for comparison to the original
    file"""
    with open("checkfile.txt", 'w', encoding='utf-8') as check_file:
        for current_artist in artists_list:
            for current_album in current_artist.albums:
                for current_song in current_album.tracks:
                    print(f"{current_artist.name}\t{current_album.name}\t"
                          f"{current_album.year}\t{current_song.name}",
                          file=check_file)


if __name__ == '__main__':
    artists = load_data()
    print(f"We have {len(artists)} artists")
    creating_check_file(artists)
