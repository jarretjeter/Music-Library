class Artist:  

    id_number = 100
    artists = []

    def __init__(self, artist, genre, birth_date):
        self.id = f"ID#: {Artist.id_number}"
        Artist.id_number = Artist.id_number + 1
        if artist in Artist.artists:
            raise ValueError(f"Artist '{artist}' already exists.")
        else:
            self.artist = f"Artist Name: {artist}"
            Artist.artists.append(artist)
        self.genre = f"Genre: {genre}"
        self.birth_date = f"Birth Date: {birth_date}"

    def __repr__(self):
        return f"{self.artist}, {self.genre}, {self.birth_date}"

    def has_artist(artist):
        if artist in Artist.artists:
            print(f"{artist} is in the list of artists")
        else:
            print(f"{artist} is not currently in the list of artists")

class Song:
    def __init__(self, title, length, lyrics):
        artist = Artist.id_number
        self.title = f"Title: {title}"
        self.length = f"Length: {length}"
        self.lyrics = f"Lyrics: {lyrics}"

    def __repr__(self):
        return f"{self.title}, {self.length}, {self.lyrics}"

mj = Artist("Michael Jackson", "Pop", "August 29, 1958")
print(mj.genre)
print(mj.id)
print(mj)


tc = Artist("Thundercat", "R&B", "October 19, 1984")
print(tc.birth_date)
print(tc.id)

artists = Artist.artists
print(artists)

them_changes = Song("Them Changes", "3:08", "Nobody move, there's blood on the floor, And I cant find my heart, Where did it go? Did I leave it in the cold? So please give it back, 'cause it's not yours to take. It must've fell when I lost my mind. Deep in the cut, drowning in a pain. Somebody help, 'cause I can't find my way Nobody move, nobody move. Somebody tell me how I'm supposed to feel. When I'm sitting here knowing this ain't real. Why in the world would I give my heart to you? Just to watch you throw it in the trash. I've been traveling so long, I don't think I can hold on. Where were you when I needed you the most? Now I'm sitting here with a black hole in my chest. A heartless, broken mess")
print(them_changes)

Artist.has_artist("Michael Jackson") 