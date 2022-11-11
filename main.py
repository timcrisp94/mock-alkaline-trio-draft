from data import songs_list
from time import sleep
import random

for song in songs_list:
    category = song['category']
    title = song['song']

def pick_random_song(player_name):
    random_song = random.choice(songs_list)
    category = random_song['category']
    song_title = random_song['song']
    print(f"In the {category} category, {player_name} picks {song_title}")

players = ["Tim", "David", "Jeremy", "Jim"]

def play_round():
    for p in players:
        sleep(1)
        pick_random_song(p)


print("Welcome to the draft")
play_round()