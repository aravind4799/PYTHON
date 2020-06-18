import xml.etree.ElementTree as ET
import sqlite3

conn=sqlite3.connect("track_db.sqlite")
cur=conn.cursor()

cur.executescript('''

   DROP TABLE IF EXISTS Artist;
   DROP TABLE IF EXISTS Genre;
   DROP TABLE IF EXISTS Album;
   DROP TABLE IF EXISTS Track;
   DROP TABLE IF EXISTS Tracks;

   CREATE TABLE Artist(
   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
   name TEXT UNIQUE
   );

   CREATE TABLE Genre(
   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
   name TEXT UNIQUE
   );

   CREATE TABLE Album(
   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
   artist_id INTEGER,
   title TEXT UNIQUE
   );

   CREATE TABLE Track(
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
   );

   ''')

def lookup(d,key):
    found=False
    for child in d:
        if found:return child.text
        if child.tag=='key' and child.text==key:
            found=True
    return None

fh=ET.parse("Library.xml")
required_data=fh.findall('dict/dict/dict')

for dict in required_data:
    if lookup(dict,'Track ID')==None:continue

    name=lookup(dict,'Name')
    artist = lookup(dict, 'Artist')
    album = lookup(dict, 'Album')
    count = lookup(dict, 'Play Count')
    rating = lookup(dict, 'Rating')
    length = lookup(dict, 'Total Time')
    genre=lookup(dict,'Genre')

    if name is None or artist is None or album is None :
          continue

    #print(name, artist, album, count, rating, length, genre)

    cur.execute("INSERT OR IGNORE INTO Artist(name) VALUES(?)",(artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id=cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Album(artist_id,title) VALUES(?,?)",(artist_id,album))
    cur.execute("SELECT id FROM Album WHERE title=?",(album,))
    album_id=cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Genre(name) VALUES(?)",(genre,))
    cur.execute("SELECT id FROM Genre WHERE name=?",(genre, ))
    genre_id=cur.fetchone()[0]

    cur.execute("INSERT OR REPLACE INTO Track(title,album_id,genre_id,len,rating,count) VALUES(?,?,?,?,?,?)",(name,album_id,genre_id,length,rating,count))

    conn.commit()

strg='''SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id
    AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3'''

for row in cur.execute(strg):
    print(str(row[0]),str(row[1]),str(row[2]),str(row[3]))
