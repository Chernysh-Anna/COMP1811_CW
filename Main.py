from Persons import Person
from FamilyTree import FamilyTree
from datetime import datetime

grandfather = Person("Walter Emmerson", birth_date=(19), death_date=())
grandmother = Person("Anna Emmerson", birth_date=(), death_date=())
father = Person("Otto Emmerson", birth_date=(), parents = [grandfather,grandmother])
mother = Person("Cornelia Emmerson", birth_date=())
child1 = Person("Alex Emmerson", parents = [mother, father])
child2 = Person("Luke Emmerson", birth_date=(), parents = [mother, father])

grandfather.add_child(father)
father.add_child(child1,child2)
FamilyTree.add_members(grandmother, grandfather, mother, father, child1, child2)

print("Parents of Otto Emmerson are", FamilyTree.find_parents(father,mother))
print("Grandchildren of Walter Emmerson are", FamilyTree.find_grandchildren(grandfather))
print("The immediate family of Otto Emmerson are", FamilyTree.find_immediate_family(father))
print("The extended family of Alex Emmerson are", FamilyTree.find_extended_family(child1))
