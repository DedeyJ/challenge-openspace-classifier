import random
import pandas as pd
from utils.table import Table


class OpenSpace():
    """The place where tables and seats are declared, and where we can assign the students to these seats
    
    :number_of_tables: number of tables in the Open Space. Specifies number of Table classes to make
    :number_of_seats: number of seats per table. Specifies number of Seat classes to make within each Table class.
    
    functions:
    - assign_seats(list_of_students: list): randomizes the student list and assigns them to a table and seat.
    - add_table()
    - display(): prints the tables, seats and students assigned to them in format:
        table_name
        seat_name : student_name 
    - seats_left(): checks for every table if there are seats still Free and counts them. returns total space left
    - make_data_frame(): puts assigned students in a dataframe to be written away in a file.
    - store(): Writes away a dataframe in an excel file
    """
    def __init__(self, number_of_tables, number_of_seats):
        """declaring our class attributes
        incoming arguments:
        :number_of_tables:
        :number_of_seats:

        declared variables:


        """
        #declaring the class attributes
        self.name = self
        self.tables = []
        self.not_assigned = []
        self.assigned_students = set()
        for i in range(1,number_of_tables+1):         #tables are created for the openspace
            name_string = "table_" + str(i)
            self.tables.append(Table(name = name_string, seats_per_table = number_of_seats)) 

    def __str__(self):
        """Method called during a conversion of the object into a chain"""
        return f"An open space for {self}"
    
    def assign_seats(self, list_of_students):
        """Method asks for list and randomly assign people to a seat
        
        :list_of_students: list of students that we want to assign to seats
        """

        #first set self.not_assigned attribute to [] to allow multiple iterations.
        self.not_assigned = []
        
        #make a list of integers in random order from 0 to length of list. every integer only once, because of sample.
        randomizer = random.sample(range(0,len(list_of_students)),len(list_of_students)) 
        
        #initilize empty list
        random_list = []
        #pick student from student list with index based on int from randomizer. append to random_list
        for i in randomizer:
            random_list.append(list_of_students[i])    

        #here we assign the students from random_list to seats. This allows students to be randomly seated.
        for student in random_list:
            if student not in self.assigned_students:
                assigned = False

                for table in self.tables:
                    for seat in table.seats:
                        if seat.free == True:
                            seat.set_occupant(student)
                            self.assigned_students.add(student)
                            assigned = True
                            break

                    if assigned:
                        break
                    
                if not assigned:
                    self.not_assigned.append(student)
    

    def add_table(self):
        """function that adds another Table object in the Open Space. Number of seats is automatically """
        #each table name is automatically given a name like table_1. we want to extract the number of the last table
        # to make a new table
        if len(self.tables) > 0:
            get_number = int(self.tables[-1].name.split("_")[1])
            name_string = "table_" + str(get_number+1)
        else:
            name_string = "table_1"
        self.tables.append(Table(name = name_string, seats_per_table = 4))


    def display(self):
        """Displays the Tables, their seats, and the people assigned to them. 
        It will also print the people not yet assigned to a table
        """
        
        print(f"Seat Assignment")
        
        for table in self.tables:
            print(table.name)
            for seat in table.seats:
                print(f"{seat.name} : {seat.student}")
        
        # checks if seats are left and prints how many if there are.
        if self.seats_left() > 0:
            print(f"There are {self.seats_left()} seats left")

        #checks if there are any students left with no seats.
        if len(self.not_assigned) > 0:
            print("\n")
            print(f"People not assigned to a table is {len(self.not_assigned)}")
            for people in self.not_assigned:
                print(people)
        else:
            print("\n")
            print("All people are assigned a table")

    def seats_left(self):
        """calculate how many seats are left at openspace.
        It does this by summing the seats left per table from Table classes.
        """
        seats_left = 0
        for table in self.tables:
            seats_left += table.left_capacity()
        return seats_left

    def make_data_frame(self):
        """Put assigned student in dataframe"""
        table_list = []
        seat_list = []
        student_list = []
        
        for table in self.tables:
            for seat in table.seats:
                if seat.free == False:
                    table_list.append(table.name)
                    seat_list.append(seat.name)
                    student_list.append(seat.student)
        
        data = {
            "Table": table_list,
            "Seat": seat_list,
            "Student": student_list
        }

        df = pd.DataFrame(data)        
        return df


    def store(self):
        """ This function stores the people assigned to the seats in a txt file
        
        :filename: the name of the file where we want to write the seat assignment to.
        """
        # Replace 'output_file.xlsx' with the desired name for your Excel file
        output_file_path = 'seat_assignment.xlsx'

        # Write the DataFrame to an Excel file
        df = self.make_data_frame()
        df.to_excel(output_file_path, index=False)


