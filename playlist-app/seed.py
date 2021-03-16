from app import app
from models import db, Playlist, Song, PlaylistSong

db.drop_all()
db.create_all()

##### Playlists #####

playlist1 = Playlist(
    name = 'Awesome',
    description = 'Awesome songs to listen to!'
)

db.session.add(playlist1)
db.session.commit()

##### Songs #####

song1 = Song(
    title = 'SQLAlchemy',
    artist = 'The Cool Cats'
)

song2 = Song(
    title = 'Postgres Rules',
    artist = 'The Cool Cats'
)

db.session.add_all([song1, song2])
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