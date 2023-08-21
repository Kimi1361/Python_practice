import csv

movies = []

title = ["Film_Red","君の名は。","時をかける少女"]
song = ["新時代","スパークル","ガーネット"]
director = ["尾田栄一郎","新海誠","細田守"]

movies.append(title)
movies.append(song)
movies.append(director)

with open("Anime2.csv","w",newline="",encoding="utf-8") as f:
    w = csv.writer(f , delimiter=",")
    for anime in movies:
        w.writerow(anime)
