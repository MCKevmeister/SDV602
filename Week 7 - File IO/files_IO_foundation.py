"""
File I/O in Python using a set of examples

https://www.geeksforgeeks.org/file-handling-python/
"""

def write_lines_to_a_file(pLines, pToFile):
    """
    Opens pToFile if it does not exists it creates it, if it exists wipes it, leaving it empty and ready to write to
    f contains file "resource" or "handle" that is used when working with the file

    Args
       pLines - a list of lines to write to the file. 
                For example pLine=[" Beautiful is better than ugly.\n",
                         "Explicit is better than implicit.\n", 
                         "Simple is better than complex.\n", 
                         "Complex is better than complicated.\n"]

        pToFile the name of the file to write to.

    """
    f=open(pToFile,"w") 
    f.writelines(pLines)
    f.close()

def read_lines_from_a_file_using_a_loop(pFromFile):
    """
    Opens pFromFile , reads it and  returns the lines as a list

    Args 
        pFromFile the name of the file to write to.
    """
    lines = []
    f=open(pFromFile,"r") 
    while True:
        line=f.readline()
        if line=='':break
        lines += [line]
    f.close()
    return lines

def read_lines_from_a_file(pFromFile):
    """
    Opens pFromFile , reads it and  returns the lines as a list

    Args 
         pFromFile the name of the file to write to.
    """
    lines = []
    f=open(pFromFile,"r") 
    lines = f.readlines()
    f.close()
    return lines

def read_lines_from_a_file_with_exception(pFromFile):
    """
    Opens pFromFile , reads it and  returns the lines as a list.

    Wraps the file output in a try: ... except: ... block , see https://docs.python.org/3/library/exceptions.html
    DO this tutorial for more learning https://docs.python.org/3/tutorial/errors.html 

    Args
        pFromFile the name of the file to read from.

    """
    try:
        lines = []
        f=open(pFromFile,"r") 
        lines = f.readlines()
        f.close()
    except FileNotFoundError:
        print ("File is not found")
 

    return lines



def read_with_iterator(pFileName):
    """
    Opens pFileName , reads it and  returns the lines as a list.

    Wraps the file output in a try: ... except: ... block , see https://docs.python.org/3/library/exceptions.html
    DO this tutorial for more learning https://docs.python.org/3/tutorial/errors.html 

    Takes advantage of "f" as an iterator

    Args
       pFileName , name of the file to read from

    """

    try:
       lines = []
       f=open(pFileName,"r")
       for line in f :
           lines += [line]

    except FileNotFoundError:
        print ("File is not found")
        return lines
    else:
        f.close()
        return lines

def append_to_file(pFileName, pAppendThese):
    """
    Appends lines in the list pAppendThese to the file pFileName.

    Args
        pFileName the file to append to
        pAppendThese a list of strings to append
    """
    try:
        lines = []
        f = open(pFileName,'a')
        f.writelines(pAppendThese)
    except FileNotFoundError:
        print ("File is not found")
    else:
        f.close()

        

def using_with_read(pFileName):
    """
    Reads a file into a list one line per list item

    Uses "with" and try catch, with removes need for f.close() "tidy up"

    Args
        pFileName - the name of the file as a string
    """ 
    
    lines = []
    try:
        with  open(pFileName,'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File is not found.")
    
    return lines        
    
     
def make_counter():
    """
    Generates two counter closures
    
    returns 
         increment, current_count
    """
    count = 0

    def increment():
        nonlocal count
        count += 1
    
    def current_count():
        nonlocal count
        return count

    return increment, current_count

def filter_direct_from_read(pFileName, **kwargs):
    """
    Filters a file line by line returning all lines that match a filter
    Uses list comprehension that applies the filter function in its "if" clause

    Args
         pFileName the name of the file
         kwargs
             "skip_header" returns the list from item 1, when set to True, default is to include the first
             "filter" a function takes a string as a parameter and returns true or false. 

    """
    filter = None
    skip_header = False
    lines =  []
    try:
        with  open(pFileName,'r') as f:
            
            if 'filter' in kwargs: # https://thispointer.com/python-how-to-check-if-a-key-exists-in-dictionary/
                filter = kwargs["filter"]     
                lines = [line for line in f.readlines() if filter(line)] 
            else :
                lines =  f.readlines() 
            
            if 'skip_header' in kwargs and kwargs['skip_header'] == True:
                lines = lines[1::]


    except FileNotFoundError:
        print("File is not found.")

    return lines

if __name__ == "__main__":
    """ Test code"""
    write_lines_to_a_file(["Beautiful is better than ugly.\n","Explicit is better than implicit.\n", 
                           "Simple is better than complex.\n", "Complex is better than complicated.\n"],
                           "Text.txt"
                         )
    # Now check Text.txt in the current directory/folder

    #print("Reading the file one line at a time, using a loop.")
    #print(read_lines_from_a_file_using_a_loop("Text.txt")) 

    #print("Reading the file into a list one item per line.")
    #print(read_lines_from_a_file("Text.txt")) 

    print("Exceptions during File I/O")
    #print(read_lines_from_a_file_with_exception("Text.txt"))
    #print(read_with_iterator("Text.txt"))

    
    print("Append list to the end of a file")
    append_to_file("Text.txt",["Another line. \n","Last Line. \n"])
    # Now check Text.txt in the current directory/folder
    
    print("Bringing in with and filter ")
    #print(using_with_read("BadFileName.txt"))
    #print(using_with_read("Text.txt"))
    
    print("Filter Direct read ")
    #print(filter_direct_from_read("BadFileName.txt"))
    print(filter_direct_from_read("Text.txt",
                                   filter= lambda x : 'Last' in x))
    print(filter_direct_from_read("Text.txt",
                                   filter= lambda x : 'Last' in x, skip_header =True))
    
    pass