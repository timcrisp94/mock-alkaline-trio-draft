from csv import DictReader


with open("draft_data.csv", 'r') as f:
  dict_reader = DictReader(f)
  songs_list = list(dict_reader)







