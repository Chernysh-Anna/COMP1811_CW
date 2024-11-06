from datetime import datetime
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

    def get_grandchildren(self, name):            #break down , not shore how to do it in more simple way
        person = self.find_person(name)
        if not person:                          #person not in thise databasse
            return []
        grandchildren = []
        for child_name in person.children:
            child = self.find_person(child_name)
            if child:
                grandchildren.extend(child.children)
        return grandchildren

    def get_close_relatives(self, name):    #break down , not shore how to do it in more simple way
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
        # all code need to be created
        pass
#-------------------------------

#F2
#------------------------

    def get_siblings(self, name):
        person = self.find_person(name)
        if person:
            return person.siblings
        return []

    def get_cousins(self, name):
        person = self.find_person(name)
        if not person:                          #person not in thise databasse
            return []
        parents = self.get_parents(name)       #find parents name/s (list)
        cousins = []
        for parent_name in parents:
            parent = self.find_person(parent_name)  #get info about parents
            if parent:
                for sibling_name in parent.siblings:
                    sibling = self.find_person(sibling_name) #get info about parents siblings
                    if sibling:
                        cousins.extend(sibling.children) #add all children to our list(cousin)
        return cousins





family_data = {
    "Alice": {"birth_date": "01-01-1980", "parents": ["Bob"], "siblings": [], "spouse": [], "children": []},
    "Bob": {"birth_date": "15-05-1975", "parents": ["bili","illy"], "siblings": ['Wob'], "spouse": [], "children": []},
    "Wob": {"birth_date": "15-05-1975", "parents": ["bili","illy"], "siblings": ['Bob'], "spouse": [], "children": ["BonBon"]}
}
family = FamilyTree(family_data)

print(family.get_cousins("Alice"))