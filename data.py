import csv

with open('draft_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      print(row['category'], row['song'])


print(row)