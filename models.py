from datetime import datetime
from dateutil.relativedelta import relativedelta
# import datetime to calculation about dates in future
class Person:
    def __init__(self, name, birth_date, death_date=None, parents=None, siblings=None, spouse=None, children=None): #<--add to atributes =None, to minimize possible KeyErrors
        self.name = name
        self.birth_date = datetime.strptime(birth_date, "%d-%m-%Y") #is strptime really help?
        self.death_date = datetime.strptime(death_date, "%d-%m-%Y") if death_date else None
        self.parents = parents or []
        self.siblings = siblings or []
        self.spouse = spouse or []
        self.children = children or []


class FamilyTree:
    def __init__(self, family_data):
        self.person = {name: Person(name, **data) for name, data in family_data.items()}   #person = people

# return object
    def find_person(self, name):
        return self.person.get(name)
#F1
#----------------------------------
# find parents
    def get_parents(self, name):                    #find parents
        person = self.find_person(name)
        if person:                                 #if person isn`t none ___ look strange but ok
            return person.parents                  #shoul return list of names
        return []

    def get_grandchildren(self, name):            #break down , how to do it in more simple way
        person = self.find_person(name)
        if not person:                          #person not in thise databasse
            return []
        grandchildren = []
        for child_name in person.children:
            child = self.find_person(child_name)
            if child:
                grandchildren.extend(child.children)
        return grandchildren

    def get_close_relatives(self, name):    #break down ,how to do it in more simple way
        person = self.find_person(name)
        if not person:
            return []
        relatives = {
            "parents": person.parents,
            "siblings": person.siblings,
            "spouse": person.spouse,
            "children": person.children
        }
        return relatives

    def get_extended_family(self, name):
        pass
        # all code need to be created
#-------------------------------

#F2
#------------------------

    def get_siblings(self, name):
        person = self.find_person(name)
        if person:
            return person.siblings
        else:
            return []

    def get_cousins(self, name):
        person = self.find_person(name)
        if not person:                          #person not in thise databasse
            return []
        parents = self.get_parents(name)       #find parents name/s (list)
        cousins = []
        for parent_name in parents:
            parent = self.find_person(parent_name)  #get info about parents
            if parent:   # no unexpected error if database not fully complete     -|but our database is perfect
                for sibling_name in parent.siblings:
                    sibling = self.find_person(sibling_name) #get info about parents siblings
                    if sibling:
                        cousins.extend(sibling.children) #add all children to our list(cousin)
        return cousins

#-----------------------

class Statistics:
    def __init__(self, family_tree):  #data may base on info from class FamilyTree
        self.family_tree = family_tree

    def get_bdays(self):
        birthdays = {}
        for name, person in self.family_tree.person.items():
            birthdays[name] = person.birth_date.strftime("%d-%m-%Y")
        return birthdays

    def get_bdays_calendar(self):
        birthday_calendar = {}
        for name, person in self.family_tree.person.items():
            day_month = person.birth_date.strftime("%d-%m")
            if day_month not in birthday_calendar:
                birthday_calendar[day_month] = []
            birthday_calendar[day_month].append(name)
        sorted_calendar = {date: birthday_calendar[date] for date in sorted(birthday_calendar.keys())}
        return sorted_calendar

    def get_children_count(self):  # get number of children for each person
        children_count = {}
        for name, person in self.family_tree.person.items():
            children_count[name] = len(person.children)
        return children_count

    def get_average_children_pp(self):   #get average children per person
        total_children = 0
        for person in self.family_tree.person.values():
            total_children += len(person.children)

        total_people = len(self.family_tree.person)
        return total_children // total_people

    def get_average_age(self):  #get average age at death
        total_age = 0
        person_count = 0
        for person in self.family_tree.person.values():  #self.person.values() doesnt work ... Why :|
            if person.death_date:
                age_at_death = relativedelta(person.death_date, person.birth_date).years   #relativedelta + .years = numerical output
                total_age += age_at_death
                person_count += 1
        return total_age // person_count  #should we check situation if person_count is 0?







#must be deleted
'''
family_data = {
    "Alice": {"birth_date": "01-01-1980", "parents": ["Bob"], "siblings": [], "spouse": [], "children": []},
    "Bob": {"birth_date": "15-05-1975", "parents": ["bili","illy"], "siblings": ['Wob'], "spouse": [], "children": []},
    "Wob": {"birth_date": "15-05-1975", "parents": ["bili","illy"], "siblings": ['Bob'], "spouse": [], "children": ["BonBon"]}
}
family_tree = FamilyTree(family_data)

#списку днів народження всіх членів сім'ї
birthdays = family_tree.get_bdays()
print("Список днів народження:", birthdays)

# календар днів народження
sorted_calendar = family_tree.get_bdays_calendar()
print("Відсортований календар днів народження:", sorted_calendar)
'''