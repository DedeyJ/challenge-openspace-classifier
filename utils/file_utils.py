import json
import sys
import tkinter as tk
from tkinter import filedialog


class file_utils():
    """Class where we put methods for reading and writing a file
    
    functions:
    - read_file(): reads a list of students
    """

    def read_file():
        """ reads the list of students from a csv file and puts it in a list """

        # Create the main window
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        # Ask the user to choose a file
        file_path = filedialog.askopenfilename(title="Select a file")

        # Check if the user selected a file or canceled the dialog
        if file_path:
            print(f"Selected file: {file_path}")
        else:
            print("File selection canceled.")

        member_list = []
        with open(file_path, "r")  as new_colleagues:
            for member in new_colleagues.read().split("\n"):
                if member  != '':
                    member_list.append(member)
        return member_list
    

    def read_json():
        # Open the JSON file
        config = './config.json'
        with open(config, 'r') as file:
            # Load the JSON data
            data = json.load(file)
        number_of_tables = data["number_of_tables"]
        number_of_seats = data["number_of_seats"]
        
        #checks if values are correct. 
        try:
            # Check if the variable is an integer
            number_of_tables = int(number_of_tables)
            # Check if the integer is larger than 0
            if number_of_tables <= 0:
                raise ValueError(f"number_of_tables must be an integer larger than 0.")
        except ValueError:
            print(f"Error: number_of_tables must be an integer larger than 0.")
            sys.exit()

        try:
            # Check if the variable is an integer
            number_of_seats = int(number_of_seats)
            # Check if the integer is larger than 0
            if number_of_seats <= 0:
                raise ValueError(f"number_of_seats must be an integer larger than 0.")
        except ValueError:
            print(f"Error: number_of_seats must be an integer larger than 0.")
            sys.exit()

        return number_of_tables, number_of_seats




