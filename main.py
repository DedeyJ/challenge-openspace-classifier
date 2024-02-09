#Import everything you need to launch the organizer
#Load the colleagues from the excel file defined in the config file
#Launch the organizer. Display the results.

#import own modules into main file
from utils.file_utils import file_utils as uti
from utils.openspace import OpenSpace as ospace
from utils.table import Table

# Read the csv file
student_list = uti.read_file()
number_of_tables, number_of_seats = uti.read_json()

#Creation of the Open Space, here we assign the amount of tables and number of seats per table. 
BeCode = ospace(number_of_tables,number_of_seats)

# Assigning the students from the list
BeCode.assign_seats(student_list)

# Shows the current seat assignment.
BeCode.display()

#Checks if all students are assigned, and keeps asking wether a new table should be added
while len(BeCode.not_assigned) > 0:
    add_table = input("Do you want to add a new table? (y/n): ")
    
    if add_table.lower() == "y":
        BeCode.add_table()
        BeCode.assign_seats(BeCode.not_assigned)
        BeCode.display()
    else:
        print("The people not assigned will need to look for another Open Space")
        break

#Write away the seating assignment to a text file.
BeCode.store()








