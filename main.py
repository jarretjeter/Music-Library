class Artist:  
    id_number = 100

    def __init__(self, name, genre, birth_date):
        self.id = Artist.id_number
        Artist.id_number = Artist.id_number + 1
        self.name = name
        self.genre = genre
        self.birth_date = birth_date

    def __repr__(self):
        return f"{self.name}, {self.genre}, {self.birth_date}"

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

tc = Artist("Thundercat", "R&B", "October 19, 1984")
print(tc.birth_date)
print(tc.id)
