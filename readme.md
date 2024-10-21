Music Player Web App
This is a web-based Music Player application that allows users to upload, play, pause, resume, stop, and delete songs. The application uses Python with Flask for the backend and HTML/CSS for the frontend.

Table of Contents
Features
Requirements
Installation
Usage
File Structure
How to Run
Screenshots
Contributing
License


Features
Upload new songs to the player.
Play, pause, resume, stop, and delete songs.
Update the list of songs in the songs.json file.
Responsive design for desktop and mobile.


Requirements
Python 3.x
Flask (Python web framework)
Pygame (for handling audio playback)


Installation
Clone the Repository:
git clone https://github.com/rachanayadavv/musicapp.git
Navigate to the Project Directory:
cd music-player-web-app
Install the Required Packages: Make sure you have Flask and Pygame installed. If not, install them using:
pip install flask pygame


Usage
File Structure
diff
Copy code
- static/
    - Closer.mp3
    - Counting_stars.mp3
    - JVKE - golden hour (Lyrics).mp3
    - Shape Of You.mp3
    - style.css
- templates/
    - index.html
- app.py
- music_player.py
- songs.json



How to Run
Run the Flask Server: Start the application by running app.py:
python app.py


Access the Application: Open your web browser and go to:
http://127.0.0.1:5000/