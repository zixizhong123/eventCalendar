'''
    Project Name: Event Calendar
    Name: Zixi Zhong
    Purpose: This program reads in a file of dates and events and creates a dictionary object that stores multiple sate
    objects, holding a date and an event list. Depending on the file input, it either just stores
    the date objects into the dictionary object, or prints out the events for a specific date.
'''


class Date:
    """
    This class creates date objects with a date and an events list
    Parameters: self, date and event list
    Returns: none but sets value to self._date and self._event
    """
    def __init__(self, date, event):
        self._date = date
        self._event = [event]


    def get_date(self):
        return str(self._date)


    def get_event(self):
        return self._event


    """
    This method adds an event to the events list
    Parameters: self and new event
    Returns: none but appends new event to the 
             event list
    """
    def add_event(self, event):
        self._event.append(str(event))


    """
    This method returns a string representation of the date object
    Parameters: self
    Returns: string representation of the date object
    """
    def __str__(self):
        return str(self._date) +", "+ str(self._event)



class DateSet:
    """
    This class creates dictionary object filled with date objects
    Parameters: self
    Returns: none but sets dictionary value to self._dict
    """
    def __init__(self):
        self._dict = {}


    """
    This method adds a date object to the dictionary's values, with
    the date string as the key
    Parameters: self and date to set the key
    Returns: none but sets the date object to the date key
    """
    def add_date(self, date):
        self._dict[date.get_date()] = date


    def get_dict(self):
        return self._dict


    """
    This method checks if the date key is already in the dictionary
    Parameters: self and date key
    Returns: True if the date is in the dictionary, False if not
    """
    def check_dict(self, date):
        return date in self._dict


    """
    This method returns a string representation of every value in 
    the dictionary object one by one
    Parameters: self
    Returns: string representation of every value in 
             the dictionary object one by one
    """
    def __str__(self):
        s = ""
        for key in self._dict.keys():
            s += str(self._dict[key]) + "\n"

        return s




def read_file(ds):
    '''
    Reads in the file and checks to see if the file line starts with
    I or R. If it starts with I, it puts the date and event into a
    date object, and then into the dictionary object. If it starts
    with an R, it prints out the associated events for that date.
    Parameters: ds - dictionary object
    Returns: none
    '''
    file = open(input())

    for line in file:
        assert line.startswith("I") or line.startswith("R"), ("ERROR: "
                                                     "Illegal operation.")
        dict = ds.get_dict()


        '''
        If the line starts with I, create a date object and add it to the 
        dictionary object
    
        If the line starts with R, prints out the events for that date 
        in the dictionary 
        '''
        if line.startswith("I"):
            i = line.find(":")   #Splits the line into a date and event
            date = line[2: i]
            canon = canonicalize_date(date) # returns a canonicalized date
            event = line[i + 1:].strip()

            '''
            Checks if the date is in the dictionary
            '''
            if ds.check_dict(canon):  # If it is, it adds the new events to
                old_date = dict[canon] # the previous date objects event list
                old_date.add_event(event) # without creating a new object

            else:
                new_date = Date(canon, event) # If not, creates a new date
                ds.add_date(new_date)         # object and adds it into the
                                              # dictionary object

        else:
            date = line[2:]  #Splits the line into a date and event
            canon = canonicalize_date(date) # returns a canonicalized date
            event = dict[canon].get_event() # Gets event from the date
            event.sort()                    # object in the dictionary object
            for i in range(len(event)):
                print("{}: {}".format(canon, event[i]))



def canonicalize_date(date_str):
    '''
    This function accepts the date formated a certain way and returns it in
    the canonical representation of the date. It asserts that the month is
    less than or equal to 12 and the day is less than or equal to 31.
    Parameters:
        date_str - string representing the date in one of several possible
                   formats
    Returns: The string in the canonical representation of the date.
    '''

    month_dict = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5,
                  "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10,
                  "Nov": 11, "Dec": 12}


    '''
    Checks the type of format the date is initially in to change it into 
    the canonicalized form
    '''
    if "-" in date_str:
        date_str = date_str.split("-")
        yyyy = date_str[0]
        mm = date_str[1]
        dd = date_str[2]
    elif "/" in date_str:
        date_str = date_str.split("/")
        yyyy = date_str[2]
        mm = date_str[0]
        dd = date_str[1]
    else:
        date_str = date_str.split()
        yyyy = date_str[2]
        mm = month_dict[date_str[0]]
        dd = date_str[1]

    assert int(mm) <= 12 and int(dd) <= 31, "ERROR: Illegal date."

    return "{:d}-{:d}-{:d}".format(int(yyyy), int(mm), int(dd))


'''
    This function creates a dictionary object and sends it to a 
    function that reads in a file either puts the date and event 
    into a date object, and then into the dictionary object, or 
    prints out the events for a date.
    
    Parameters: None 
    Returns: None
'''
def main():
    ds = DateSet()

    read_file(ds)


main()