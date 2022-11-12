import random
from data import songs_list

class Player:
    def __init__(self, name):
        self.name = name
        self.songs = {
          "Asian_Man": "",
          "Vagrant": "",
          "Epic_taph": "",
          "First_Songs": "",
          "Remains": "",
          "Wild_Card": "",
          "Dan_Song": ""
        }

    def add_song(self):
        song = random.choice(songs_list)
        category = song["category"]
        song_title = song["song"]

        if self.songs[category] == "":
            self.songs[category] = song_title
        else:
          self.add_song()

        return self.songs
        
