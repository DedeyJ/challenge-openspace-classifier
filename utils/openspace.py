
from utils.table import Table
import random 


class OpenSpace():
    """The place where tables and seats are declared, and where we can assign the students to these seats
    
    functions:
    - assign_seats(): randomizes the student list and assigns them to a table and seat.
    - display(): prints the tables, seats and students assigned to them in format:
        table_name
        seat_name : student_name 
    """
    def __init__(self, number_of_tables, number_of_seats):
        self.name = self
        # while True:             #Keep asking for input until number is given. No solution yet for values O and below
        #     try:
        #         qty_tables = int(input("How many tables are there?: "))
        #         break
        #     except ValueError:
        #         print("Invalid Input. please enter a valid number")


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
        self.not_assigned = []
        randomizer = random.sample(range(0,len(list_of_students)),len(list_of_students))        #list of numbers in random order
        random_list = []
        for i in randomizer:
            random_list.append(list_of_students[i])     #Put student using random list created earlier

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
        get_number = int(self.tables[-1].name.split("_")[1])
        name_string = "table_" + str(get_number+1)
        self.tables.append(Table(name = name_string, seats_per_table = 4))

    def display(self):
        """Displays the Tables, their seats, and the people assigned to them. 
        It will also print the people not yet assigned to a table
        """
        seats_left = 0
        print(f"Seat Assignment")
        for table in self.tables:
            print(table.name)
            for seat in table.seats:
                print(f"{seat.name} : {seat.student}")
        

        if self.seats_left() > 0:
            print(f"There are {self.seats_left} seats left")

        if len(self.not_assigned) > 0:
            print("\n")
            print(f"People not assigned to a table is {len(self.not_assigned)}")
            for people in self.not_assigned:
                print(people)
        else:
            print("\n")
            print("All people are assigned a table")

    def seats_left(self):
        seats_left = 0
        for table in self.tables:
            seats_left += table.left_capacity()
        return seats_left

    def store(self, filename):
        """ This function stores the people assigned to the seats in a txt file
        
        :filename: the name of the file where we want to write the seat assignment to.
        """
        output_file = "./" + filename
        with open(output_file,"w") as clear_file:
            clear_file.write("Seat Assignment")
        for table in self.tables:
            for seat in table.seats:
                with open(output_file, "a") as table_assigment:
                    table_assigment.write(f"{table.name} - {seat.name} - {seat.student}\n")

