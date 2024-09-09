# Saul's Monthly Spotify Playlist creation tool

## Setup
### Code Setup
#### Clone the repository:<br>

   <code>git clone https://github.com/Saul-Harwin/Monthly-Spotify-Playlist.git {Directory}</code>

### Spotify Setup
#### 1. Navigate to <a>https://developer.spotify.com/dashboard</a>
#### 2. Creating the app
  Click <strong>Create App</strong>
#### 3. Fill in the from
  The only important part of the form is the <strong>Redirect URIs</strong> box where you will want to add http://127.0.0.1:5000 
#### 4. Hit Save

### Editting the constants file
1. Firstly we will need the client_id and the client_secret so navigate back to the developer dashboard 
<a>https://developer.spotify.com/dashboard</a>
2. Navigate to the constants file<br>
   <code>nano Monthly-Spotify-Playlist/constants.py</code>
2. Copy both the client_id and client_secret and paste them in the respected sections in the constants file
3. Then add your spotify username to the username variable which can be found in the spotify app

## Run
It is reccommended to run this program in a virtual environment.
### Creating a virtual environment
   <code>python -m venv venv</code>

   <code>source ./venv/bin/activate</code>
### Install the requirements:
  <code>pip install -r requirements.txt</code>
### Running Code
  <code>python3 ./run.py</code>

## Scheduling task 
To best enjoy this application it is recommended to schedule the running of the script every hour. If on a linux system the best way of doing this is with cronjobs. 
### 1. Open a new cronjob
Enter into a terminal window: <br>
<code>crontab -e</code><br>
Then at the bottom of the file add this line<br>
<code>0 * * * * {Path_to_Folder}/Monthly-Spotify-Playlist/venv/bin/python3 {Path_to_Folder}/Monthly-Spotify-Playlist/run.py >> {Path_to_Folder}/Monthly-Spotify-Playlist/log.txt 2>&1</code>
