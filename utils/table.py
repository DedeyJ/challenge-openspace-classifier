

class Seat():
    def __init__(self, name, table_name):
        """ This is a seat"""
        self.name = name        #gives name to seat
        self.student = None
        self.table_name = table_name
        self.free = True        #set seat open while first created
    
    def __str__(self):
        """Method called during a conversion of the object into a chain"""
        return f"This is {self.name} for {self.table_name}."

    def set_occupant(self, student):   #function to set person in seat
        """Assign an occupant to the seat"""
        self.student = student
        self.free = False

    # def remove_occupant(self):
    #     """removes an occupant if there"""
    #     if self.occupant is None:
    #         print("This seat has no occupant")
    #     else:
    #         self.last_occupant = self.occupant
    #         self.occupant = None
    #         self.free = True
    #         return self.last_occupant
        


class Table():
    def __init__(self, name, seats_per_table):
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
    
    # def assign_seat(self, counter: int, people_not_seated: list, name: str):
    #     """assigns a seat to a student if possible"""
    #     for i in self.seats:
    #         if i.free == True:
    #             i.set_occupant(name)
    #             break
    #         else:
    #             counter +=1
    #             people_not_seated.append(name)
    #             return (counter, people_not_seated)

    def left_capacity(self):
        space = sum([1 for i in self.seats if i.free == True ])
        return space

    # def has_free_spot(self):
    #     if  sum([self.seats.free]) > 0:
    #         return True


