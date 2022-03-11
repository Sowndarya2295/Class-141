from flask import Flask,jsonify,request
import csv
all_movie = []
with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]    
    
liked_movies = []
not_liked_movies = []
did_not_watch = []
app = Flask(_name_)



