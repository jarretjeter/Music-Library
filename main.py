class Artists:
    def __init__(self, id, name, genre, birth_date):
        self.id = id
        self.name = name
        self.genre = genre
        self.birth_date = birth_date

class Songs:
    def __init__(self, artist, title, length, lyrics):
        self.artist = artist
        self.title = title
        self.length = length
        self.lyrics = lyrics