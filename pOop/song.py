class Song:
    """This is class to represent a song

    Attributes:
        title(str): The title of the song.
        artist(Artist): object to represent the song's creator.
        duration(optional[int]): Duration of the song in secs.
            Will default to zero if not specified.
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """class to represent album using track's list
    Attributes:
        name(str): the name of the album
        year(int): the year in which the album was released
        artist(Artist): Name of the artist responsible for the album. If
            not specified will default to name 'various artist'.
        tracks(List[Song]): list of the song for the current album

    Methods:
        add_song: this will add song to the album's tracks list
    """

    def __init__(self, name, year, artist=None):
        """Initialises class `Album` """

        self.name = name
        self.year = year
        if artist:
            self.artist = artist
        else:
            self.artist = Artist('various artist')
        self.tracks = []

    def add_song(self, song, position=0):
        """adds song to the track list
            Args:
                song(Song): song object to be added to track list
                position(int): position on which the song should be added on
                    (If specified). Otherwise, it will be added on the
                    end of the list.
        """
        if position:
            self.tracks.insert(position, song)
        else:
            self.tracks.append(song)


class Artist:
    """"Basic class to store artist details

    Attributes:
        name(str): Name of the artist
        albums(List[Album]): list of albums responsible for the artist. The
            list only shows album in this collection.

    Methods:
        add_album: used to add album to the collection (artist's album list)
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        """Add album to the artist's album list.
            :param album: album object to be added to the list.
                if the album already exist won't be added again (yet to
                be implemented).
        """

        self.albums.append(album)


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
    current_artist = None
    current_album = None
    artist_list = []
    with open(file_name, 'r', encoding='utf-8') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(
                line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)

            if current_artist is None:
                current_artist = Artist(artist_field)
                artist_list.append(current_artist)
            elif current_artist.name != artist_field:
                # we've just read details for new artist
                # Retrieve current artist if already exist in the artist list
                # if not current (new) artist object will be created and appended
                current_artist = find_object(artist_field, artist_list)
                if current_artist is None:
                    current_artist = Artist(artist_field)
                    artist_list.append(current_artist)
                    current_artist.add_album(current_album)
                current_album = None

            if current_album is None:
                current_album = Album(album_field, year_field, current_artist)
                current_artist.add_album(current_album)
            elif current_album.name != album_field:
                # we've just read new album for the current artist
                # Retrieve album if already exist,
                # Otherwise, create current(new) album object and store it the
                # artist's collection
                current_album = find_object(album_field, current_artist.albums)
                if current_album is None:
                    current_album = Album(album_field, year_field, current_artist)
                    current_artist.add_album(current_album)

            # creating new (current) song object and add it to the current
            # album's collection
            current_song = Song(song_field, current_artist)
            current_album.add_song(current_song)

    return artist_list


def creating_check_file(artists_list):
    """creating check file from the object data for comparison to the original
    file"""
    with open("checkfile.txt", 'w', encoding='utf-8') as check_file:
        for current_artist in artists_list:
            for current_album in current_artist.albums:
                for current_song in current_album.tracks:
                    print(f"{current_artist.name}\t{current_album.name}\t"
                          f"{current_album.year}\t{current_song.title}",
                          file=check_file)


if __name__ == '__main__':
    artists = load_data()
    print(f"We have {len(artists)} artists")
    creating_check_file(artists)
