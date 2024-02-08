from utils.file_utils import file_utils as uti
from utils.openspace import OpenSpace as ospace
from utils.table import Table


list_openspace = []
student_list = uti.read_file()

BeCode = ospace()
list_openspace = [BeCode]
not_assigned = BeCode.assign_seats(student_list)
BeCode.display()
print(not_assigned)

def write_file():
    output_file = "./table_assignment.txt"
    for table in list_openspace[0].tables:
        for seat in table.seats:
            with open(output_file, "a") as table_assigment:
                table_assigment.write(f"{table.name} - {seat.name} - {seat.student}\n")
write_file()








