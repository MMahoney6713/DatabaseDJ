from unittest import TestCase

from app import app
from models import db, Playlist, Song, PlaylistSong


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist_test'
app.config['SQLALCHEMY_ECHO'] = False
app.config['TESTING'] = True

db.session.rollback()

class PlaylistRoutesTestCase(TestCase):
    
    def setUp(self):
        self.client = app.test_client()
        seed_test_db()

    def tearDown(self):
        db.drop_all()
        db.session.rollback()

    def test_show_all_playlists_should_render_list_of_all_playlist_names(self):
        with self.client:
            
            response = self.client.get("/playlists")

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'PlaylistName1', response.data)
            self.assertIn(b'PlaylistName2', response.data)

    def test_show_playlist_should_render_one_playlist_with_detail(self):
        with self.client:
            
            response = self.client.get("/playlists/1")

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'PlaylistName1', response.data)
            self.assertIn(b'PlaylistDescription1', response.data)

    def test_add_playlist_should_render_form_on_GET(self):
        with self.client:
            
            response = self.client.get("/playlists/add")

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'form-control', response.data)
            self.assertIn(b'Name', response.data)
            self.assertIn(b'Description', response.data)

    def test_add_playlist_should_redirect_with_new_playlist_added_on_POST(self):
        with self.client:
            playlist_data = {
                "name": "PlaylistName3",
                "description": "PlaylistDescription3"
            }

            response = self.client.post("/playlists/add", data=playlist_data, follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'PlaylistName3', response.data)


class SongRoutesTestCase(TestCase):

    def setUp(self):
        self.client = app.test_client()
        seed_test_db()

    def tearDown(self):
        db.drop_all()
        db.session.rollback()

    def test_show_all_songs_should_render_list_of_all_song_titles(self):
        with self.client:
            
            response = self.client.get("/songs")

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'SongTitle1', response.data)
            self.assertIn(b'SongTitle2', response.data)

    def test_show_song_should_render_one_song_with_detail(self):
        with self.client:
            
            response = self.client.get("/songs/1")

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'SongTitle1', response.data)
            self.assertIn(b'Artist1', response.data)

    def test_add_song_should_render_form_on_GET(self):
        with self.client:
            
            response = self.client.get("/songs/add")

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'form-control', response.data)
            self.assertIn(b'Title', response.data)
            self.assertIn(b'Artist', response.data)

    def test_add_song_should_redirect_with_new_song_added_on_POST(self):
        with self.client:
            song_data = {
                "title": "SongTitle4",
                "artist": "Artist4"
            }

            response = self.client.post("/songs/add", data=song_data, follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'SongTitle4', response.data)

    def test_add_song_to_playlist_should_render_form_on_GET(self):
        with self.client:
            
            response = self.client.get("/playlists/1/add-song")

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'form-control', response.data)
            self.assertIn(b'PlaylistName1', response.data)

    def test_add_song_to_playlist_should_redirect_with_new_song_added_on_POST(self):
        with self.client:
            song_data = {
                "song": "3"
            }

            response = self.client.post("/playlists/1/add-song", data=song_data, follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'SongTitle3', response.data)




def seed_test_db():

    db.drop_all()
    db.create_all()

    ##### Playlists #####
    playlist1 = Playlist(
        name = 'PlaylistName1',
        description = 'PlaylistDescription1'
    )
    playlist2 = Playlist(
        name = 'PlaylistName2',
        description = 'PlaylistDescription2'
    )

    db.session.add_all([playlist1, playlist2])
    db.session.commit()

    ##### Songs #####
    song1 = Song(
        title = 'SongTitle1',
        artist = 'Artist1'
    )
    song2 = Song(
        title = 'SongTitle2',
        artist = 'Artist2'
    )
    song3 = Song(
        title = 'SongTitle3',
        artist = 'Artist3'
    )
    

    db.session.add_all([song1, song2, song3])
    db.session.commit()

    ##### Playlist/Song Connections #####
    playlist_song1 = PlaylistSong(
        playlist_id = 1,
        song_id = 1
    )

    playlist_song2 = PlaylistSong(
        playlist_id = 1,
        song_id = 2
    )

    db.session.add_all([playlist_song1, playlist_song2])
    db.session.commit()