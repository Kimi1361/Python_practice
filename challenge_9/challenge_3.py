import csv

movies = []

title = ["Film_Red","Your Name","Girl Who Leapt Through Time"]
song = ["New age","Sparkle","Garnet"]
director = ["Eiichiro Oda","Makoto Shinkai","Mamoru Hosoda"]

movies.append(title)
movies.append(song)
movies.append(director)

with open("Anime.csv","w",newline="") as f:
    w = csv.writer(f , delimiter=",")
    w.writerow(title)
    w.writerow(song)
    w.writerow(director)
