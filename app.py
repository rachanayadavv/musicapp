from flask import Flask, render_template, jsonify, request
import pygame
import json
import os

# Initialize Pygame for audio playback
pygame.mixer.init()

# Create a Flask app instance
app = Flask(__name__)

# Load songs from the JSON file
songs_file_path = 'songs.json'
if os.path.exists(songs_file_path):
    with open(songs_file_path, 'r') as file:
        songs = json.load(file)
else:
    songs = {}  # Initialize with an empty dictionary if the file does not exist

# Track the currently playing song
current_song = None

# Home route to display a list of available songs
@app.route('/')
def home():
    return render_template('index.html', songs=songs)

# Route to play a selected song
@app.route('/play', methods=['POST'])
def play_song():
    global current_song
    song_name = request.json.get('song_name')
    song_path = songs.get(song_name)
    if song_path:
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        current_song = song_name
        return jsonify({"status": "playing", "song_name": song_name})
    return jsonify({"status": "error", "message": "Song not found"}), 400

# Route to pause the currently playing song
@app.route('/pause', methods=['POST'])
def pause_song():
    pygame.mixer.music.pause()
    return jsonify({"status": "paused"})

# Route to resume the paused song
@app.route('/resume', methods=['POST'])
def resume_song():
    pygame.mixer.music.unpause()
    return jsonify({"status": "resumed"})

# Route to stop the currently playing song
@app.route('/stop', methods=['POST'])
def stop_song():
    pygame.mixer.music.stop()
    return jsonify({"status": "stopped"})

# Route to add a new song
@app.route('/add_song', methods=['POST'])
def add_song():
    if 'song_file' not in request.files:
        return jsonify({"status": "error", "message": "No file part"}), 400

    file = request.files['song_file']
    if file.filename == '':
        return jsonify({"status": "error", "message": "No selected file"}), 400

    if file.filename in songs:
        return jsonify({"status": "error", "message": "Song already exists"}), 400

    song_path = os.path.join('static', file.filename)
    file.save(song_path)

    songs[file.filename] = song_path

    with open(songs_file_path, 'w') as file:
        json.dump(songs, file)

    return jsonify({"status": "success"})

# Route to delete a song
@app.route('/delete_song', methods=['POST'])
def delete_song():
    song_name = request.json.get('song_name')
    
    if song_name in songs:
        song_path = songs[song_name]
        if os.path.exists(song_path):
            os.remove(song_path)
        
        del songs[song_name]

        with open(songs_file_path, 'w') as file:
            json.dump(songs, file)

        return jsonify({"status": "success", "message": f"{song_name} deleted successfully!"})
    
    return jsonify({"status": "error", "message": "Song not found!"}), 400

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
