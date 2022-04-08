class Artist:  
    id_number = 000

    def __init__(self, name, genre, birth_date):
        self.id = Artist.id_number
        Artist.id_number = Artist.id_number + 1
        self.name = name
        self.genre = genre
        self.birth_date = birth_date

class Song:
    def __init__(self, artist, title, length, lyrics):
        self.artist = artist
        self.title = title
        self.length = length
        self.lyrics = lyrics

mj = Artist("Michael Jackson", "Pop", "August 29, 1958")
print(mj.genre)
print(mj.id)

tc = Artist("Thundercat", "R&B", "October 19, 1984")
print(tc.birth_date)
print(tc.id)
