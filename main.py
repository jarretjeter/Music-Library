class Artist:  

    id_number = 100
    artists = []

    def __init__(self, artist, genre, birth_date):
        self.id = Artist.id_number
        Artist.id_number = Artist.id_number + 1
        if artist in Artist.artists:
            raise ValueError(f"Artist '{artist}' already exists.")
        else:
            self.artist = artist
            Artist.artists.append(artist)
        self.genre = genre
        self.birth_date = birth_date

    def __repr__(self):
        return f"{self.artist}, {self.genre}, {self.birth_date}"

class Song:
    def __init__(self, artist, title, length, lyrics):
        self.artist = artist
        self.title = title
        self.length = length
        self.lyrics = lyrics

    def __repr__(self):
        return f"{self.title}, {self.length}, {self.lyrics}"

mj = Artist("Michael Jackson", "Pop", "August 29, 1958")
print(mj.genre)
print(mj.id)
print(mj)

mjackson = Artist("Michael Jackson", "Pop", "August 29, 1958")

tc = Artist("Thundercat", "R&B", "October 19, 1984")
print(tc.birth_date)
print(tc.id)
