

class Seat():
    """Here is a seat, is assigned to a Table object"""
    def __init__(self, name, table_name):
        """ This is a seat
        
        :name: a unique name for the seat
        :table_name: to tell which table it belongs. (not needed yet)

        variables:
        self.free is set to Free when first made. No one sits here yet.
        """
        #declare attributes
        self.name = name 
        #student attribute is not yet filled     
        self.student = None
        self.table_name = table_name
        #tells us if its free, is free when created
        self.free = True      
    
    def __str__(self):
        """Method called during a conversion of the object into a chain"""
        return f"This is {self.name} for {self.table_name}."

    def set_occupant(self, student):   #function to set person in seat
        """Assign an occupant to the seat"""
        self.student = student
        self.free = False


class Table():
    """This is a table object. It has a name, and has seats assigned to it."""
    def __init__(self, name: str, seats_per_table: int):
        """Here we initialize the attributes when creating a new Table object
        
        input variables:
        :name: to give it a unique name.
        :seats_per_table: used to assign a number of Seat objects in a list.


        """
        self.name = name
        self.seats_per_table =  seats_per_table
        self.seats = []
        for seat in range(1,seats_per_table+1):
            name_string = "seat_" + str(seat)
            self.seats.append(Seat(name = name_string, table_name = self.name))
        self.students_assigned = []

    def __str__(self):
        """Method called during a conversion of the object into a chain"""
        return f"This is {self.name}."
    
    def left_capacity(self):
        """Checks how many seats are free in this table. return the value"""
        #create a list filled with elements of 1 for seats that are free in the Table and adds them up
        space = sum([1 for i in self.seats if i.free == True ])
        return space
        


