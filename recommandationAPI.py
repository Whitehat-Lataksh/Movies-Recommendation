from flask import Flask, json, jsonify, request
import pandas
import csv


movies_data = []
data = []


with open ('Movies_Data.csv', encoding='utf-8') as f:
    reader  = csv.reader(f)
    for i in reader:
        data.append(i)

movies_data = data[1:]

likedMovies = [ ]
unlikedMovies = [ ]
NotWatchedMovies = [ ]


app = Flask(__name__)

# Routes

@app.route('/getMovie')
 
def getMovie():
    return jsonify({
        'data' : movies_data[0],
        'message' : 'success'
    }), 200


@app.route('/likeMovie', methods=["POST"])

def likeMovie():
    movie = movies_data[0]
    Movies_data1 = movies_data[1:]
    likedMovies.append(movie)

    return jsonify({
        'status' : 'success',
        'movie_name' : likedMovies
    }), 200


@app.route('/unlikeMovie', methods = ['POST'])

def unlikeMovie():
    movie = movies_data[0]
    unlikedMovies.append(movie)

    return jsonify({
        'status' : 'success',
        'movie' : unlikedMovies
    }), 200


@app.route('/notWatched', methods = ['POST'])

def notwatched():
    movie = movies_data[0]
    Movies_data = movies_data[1:]
    NotWatchedMovies.append(movie)

    return jsonify({
        'status' : 'success'
    }), 200



if __name__ == "__main__":
    app.run(debug=True)



