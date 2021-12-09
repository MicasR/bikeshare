This flask app analyzes bikeshare data for Chicago, New York, and Washington DC.  I use python3.96, and other dependencies are in the requirements.txt file.

To run the project first, download the flies and ensure you have the correct python version.

Open a terminal and change the directory to the project folder. Run the command bellow to create a virtual environment

$python3 -m venv venv

Activate the virtual environment by running:
$ source venv/bin/activate

Install the dependencies on the requirements.txt
$ pip install requirements.txt


After this, run the flask app:
$ flask run

Open the browser and go to:
http://127.0.0.1:5000/

The link will open the filtering session. Select the information desired and click on the Query button at the end of the page. After the click, the system will take you to the Dashboard page, where the query and analysis are.

At the bottom of the page are two buttons that allow you to view more rows of the data.




