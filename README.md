# README
## _Open Space classifier_

### Description
In this small project, we create an Open Space, assign it tables and amount of seats from a json file. we attempt to randomly assign people from a list in a csv file to those seats in an open space. For this exercise we assume that all tables have the same amount of seats.

### Requirements
This program runs best in the latest python 3.12 environment.

requires pandas module:
To instal from windows with pip:
~~~
pip install pandas
~~~

### Installation
Download or pull this repository to your local drive. 

You can change the setup of your Open Space room by changing config.json file.
Below the standard setup of the json file. Change the numbers to your preference:
{
    "number_of_tables": 5,
    "number_of_seats": 4
}


Open your Terminal in the folder containing the main.py file and write following code to run program:
~~~
python3 main.py 
~~~

### Usage
As stated above program is run from Terminal by using code:
~~~
python3 main.py 
~~~

It will create an Open Space with tables and seats specified in config.json.
It will then ask to give in a file with the list of students you want to assign, will put those in a list and have them assigned to the tables and seats.
If there are not enough seats available, it will ask to add another table. If yes, then another table is added with 4 seats and we assign not yet assigned students to these seats. It will keep asking until all students are assigned a seat or until we don't add any more tables.

In the end, it writes the seating assignment away in a xlsx file in the parent directory.