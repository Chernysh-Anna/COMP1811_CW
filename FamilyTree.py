from Persons import Person
from Utils import calculate_average

class FamilyTree:
    def __init__(self):
        self.members = []

    def add_members(self, Persons):
        self.members.append(Persons)       #Adds a person.

    def find_parents(self, Persons):       #Returns the parent of the person.
        return Persons.parents
    
    def find_grandchildren(self, Persons):   #Returns grandchildren of the person.
        grandchildren = []
        for child in Persons.children:
            grandchildren.extend(child.children)
        return grandchildren
    
    def find_immediate_family(self, Persons):    #Returns immediate family, like parents, sbilings, spouse and children.
        immediate_family = set(Persons.parents)
        immediate_family.update(self.find_siblings(Persons))
        if Persons.spouse:
            immediate_family.add(Persons.spouse)
        immediate_family.update(Persons.children)
        return list(immediate_family)
    
    def find_extended_family(self, Persons):    #Returns extended family like aunt and uncle.
        extended_family = set(self.find_immediate_family)
        for parent in Persons.parents:
            aunt_uncle = self.find_siblings(parent)
            extended_family.update(aunt_uncle)

            for aunt_uncle in aunt_uncle:
                extended_family.update(aunt_uncle.childre)

        return list(extended_family)
       