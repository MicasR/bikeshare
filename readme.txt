This flask app analyzes bikeshare data for Chicago, New York, and Washington DC.
I use python3.96, and other dependencies are in the requirements.txt file.

=============================================
HOW TO RUN APP
=============================================

1. Download the flies and ensure you have the correct python(3.96) version.
https://github.com/MicasR/bikeshare.git


2. Unzip the download folder


3. Save the folder on a convenient location like desktop.


4. Open a terminal and change the directory to the project folder.
I used a WSL (a linux machine on windows)


5. Run the command bellow to create a virtual environment:
$python3.9 -m venv venv


6. Activate the virtual environment by running:
$source venv/bin/activate


7.Install the dependencies on the requirements.txt
$ pip install -r requirements.txt


8.Run the flask app:
$ flask run


7. Open the browser and go to:
http://127.0.0.1:5000/

=============================================

The link will open the filtering session. Select the information desired and click on the Query button at the end of the page. 
After the click, the system will take you to the Dashboard page, where the results are.

At the bottom of the page are two buttons that allow you to view more rows of data.
