# This program is an example of class inheritance , get and set methods.

from datetime import datetime, date

today = date.today()
print(today)

class Human:
    """Main class."""

    def __init__(self, first_name, last_name, date_of_birth):  # Class constructor.
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth


    def set_age(self):
        currentdate = datetime.datetime.today().date()
        date_of_birth = datetime.date.strptime(date_of_birth, "%d/%m/%Y").date()
        age = currentdate.year - date_of_birth.year
        monthveri = currentdate.month - date_of_birth.month
        dateveri = currentdate.day - date_of_birth.day

        #Type conversion here
        age = int(age)
        monthveri = int(monthveri)
        dateveri = int(dateveri)

        # some decisions
        if monthveri < 0 :
            age = age-1
        elif dateveri < 0 and monthveri == 0:
            age = age-1

        return age
class Pupil(Human):
    """ Pupil's introduction."""

    def __init__(self, first_name, last_name, date_of_birth, school_class):
        Human.__init__(self, first_name, last_name, date_of_birth)
        age = Human.set_age(self)
        self.school_class = school_class

#        age = Pupil.set_age()
#        print('"Pupil\'s data: " {0} {1} {2} {3})'.format(first_name, last_name, age, school_class), end=" ")


class Parent(Human):
    """ Parent's introduction."""

    def __init__(self, first_name, last_name, date_of_birth, work, working_address):
        Human.__init__(self, first_name, last_name, date_of_birth)
        self.work = work
        self.working_address = working_address
        age = Human.set_age(self)
        print( '"Parent\'s data: " {0} {1} {2} {3} {4} )'.format(first_name, last_name, age, work, working_address),
            end=" ")


pupil = Pupil('Ivan', 'Ivanov', 2011/7/22, '2 G')
parent = Parent('Peter', 'Petrov', 1995/7/22, 'BSU', 'Minsk')
print()