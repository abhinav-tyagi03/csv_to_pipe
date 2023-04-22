# csv_to_pipe
Python == 3.9.x

To install requirements :-
pip install -r requirements.txt

To run the api:-
uvicorn app:app --reload

To test the api:-
go the the port on which api is running and add :-
/docs
to the url. Then, click on try it out button.

To convert csv to pipe, make sure api is running in background.
Open main.html and upload the csv file.
Click on submit.
The pipe delimited text file will be stored in the directory in which api is running.
