from datetime import datetime

class Person:
    def __init__(self,name:str, birth_date, death_date=None):
        self.name = name
        self.birth_date = birth_date
        self.death_date = death_date
        self.parents = []     #List of Parents
        self.children = []    #List of children
        self.spouse = []      #List of Spouse

    def add_child(self,child):
        self.children.append(child)    #Adds a child to the person's children list.

    def add_spouse(self,spouse):
        self.spouse=spouse             #Adds a spouse for the person.

    def death_age (self):
        if self.death_date:
            return (self.death_date-self.birth_date).days // 365
        return None
    def __repr__(self):
        return Person(name={self.name}, birth_date={self.birth_date.strftime('%d-%m-%y')})
    
