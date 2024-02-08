
from utils.table import Table
from utils.file_utils import file_utils as fu
import random 


class OpenSpace():
    """The place where tables and seats are declared, and where we can assign the students to these seats
    
    functions:
    - assign_seats(): randomizes the student list and assigns them to a table and seat.
    - display(): prints the tables, seats and students assigned to them in format:
        table_name
        seat_name : student_name 
    """
    def __init__(self):
        qty_tables = int(input("How many tables are there?: "))
        self.tables = []
        self.assigned_students = set()
        for i in range(1,qty_tables+1):
            name_string = "table_" + str(i)
            self.tables.append(Table(name = name_string, seats_per_table=4)) 

    def __str__(self):
        """Method called during a conversion of the object into a chain"""
        return f"An open space for {self}"
    
    def assign_seats(self, list_of_students):
        """Method asks for list and randomly assign people to a seat
        
        :list_of_students: list of students that we want to assign to seats
        """
        randomizer = random.sample(range(0,len(list_of_students)),len(list_of_students))        #list of numbers in random order
        random_list = []
        for i in randomizer:
            random_list.append(list_of_students[i])     #Put student in 

        people_not_seated = []

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
                    people_not_seated.append(student)

        return people_not_seated
    
               
    def display(self):
        """Displays the Tables, their seats, and the people assigned to them"""
        for table in self.tables:
            print(table.name)
            for seat in table.seats:
                print(f"{seat.name} : {seat.student}")


    # def store(filename):


