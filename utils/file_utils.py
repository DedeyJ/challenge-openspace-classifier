

class file_utils():
    """Class where we put methods for reading and writing a file
    
    functions:
    - read_file(): reads a list of students
    """
    def read_file():
        """ reads the list of students from a csv  file """
        import_file = "./new_colleagues.csv"
        member_list = []
        with open(import_file, "r")  as new_colleagues:
            for member in new_colleagues.read().split("\n"):
                if member  != '':
                    member_list.append(member)
        return member_list
    

