class Song:
    count = 0
    genre_count = {}
    artist_count = {}
    genres = set()
    artists = set()

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1

        # Update genre_count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Update artist_count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

        # Update genres and artists set
        Song.genres.add(genre)
        Song.artists.add(artist)


class TestSong:
    '''Class "Song" in song.py'''

    def test_saves_name_artist_genre(self):
        '''instantiates with a name, artist, and genre.'''
        out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
        assert out_of_touch.name == "Out of Touch"
        assert out_of_touch.artist == "Hall and Oates"
        assert out_of_touch.genre == "Pop"

    def test_has_song_count(self):
        '''counts the total number of Song objects.'''
        assert Song.count == 4
        Song("Sara Smile", "Hall and Oates", "Pop")
        assert Song.count == 5

    def test_has_genres(self):
        '''keeps track of all Song genres.'''
        assert "Rap" in Song.genres
        assert "Pop" in Song.genres
        assert "Rock" in Song.genres

    def test_has_artists(self):
        '''keeps track of all Song artists.'''
        assert "Jay Z" in Song.artists
        assert "Beyonce" in Song.artists
        assert "Hall and Oates" in Song.artists

    def test_has_genre_count(self):
        '''keeps count of Songs for each genre.'''
        assert Song.genre_count["Rap"] == 1
        assert Song.genre_count["Pop"] == 3
        assert Song.genre_count["Rock"] == 1

    def test_has_artist_count(self):
        '''keeps count of Songs for each artist.'''
        assert Song.artist_count["Jay Z"] == 1
        assert Song.artist_count["Beyonce"] == 1
        assert Song.artist_count["Nirvana"] == 1
        assert Song.artist_count["Hall and Oates"] == 2
