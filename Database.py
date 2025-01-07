"""
Author: Anna Chernysh , Krishna Tamang
Date: 25.11.2024

Based on the requirements from the coursework, we created a module that provides a system for analyzing family relationships
using Python.It consists of the `Person` and `FamilyTree` classes that represent information about individuals and their
family relationships, as well as the `Statistics` class for creating family-wide information such as average age, number
of children, and birthday calendars.

Key Features:
- Represent individuals with personal information (name, date of birth, date of death, etc.).
- Track family relationships, including parents, siblings, cousins, and extended family members.
- Calculate and extract family statistics such as average age, average number of children, and birthday calendars.
"""

from datetime import datetime
from Data import family_data

# Represents an individual in the family tree
class Person:
    def __init__(self, name, birth_date, death_date=None, parents=None, spouse=None, children=None):
        """
            Initializes a Person instance.

            Attributes:
                name (str): Name of the person.
                birth_date (str): Birth date in the format 'DD-MM-YYYY'.
                death_date (str): Death date in the format 'DD-MM-YYYY'. Defaults to None.
                parents (list): Names of the person's parents. Defaults to an empty list.
                spouse (list): Names of the person's spouse. Defaults to an empty list.
                children (list): Names of the person's children. Defaults to an empty list.
        """
        self.name = name
        self.birth_date = datetime.strptime(birth_date, "%d-%m-%Y")
        self.death_date = datetime.strptime(death_date, "%d-%m-%Y") if death_date else None
        self.parents = parents or []
        self.spouse = spouse or []
        self.children = children or []

# family relationship
class FamilyTree:
    def __init__(self, family_data):
        self.person = {name: Person(name, **data) for name, data in family_data.items()}

    def find_person(self, name):
        """
        Finds a person by name.

        Parameters:
            name (str): Name of the person to find.

        Returns:
            Person or None: The Person object if found, otherwise None.
        """

        return self.person.get(name)


    def get_parents(self, name):
        """
        Find parents of a person.

        Parameters:
            name (str): Name of the person.

        Returns:
            list: Names of the person's parents.
        """
        person = self.find_person(name)
        return person.parents

    def get_grandchildren(self, name):
        """
        Find the grandchildren of a person.

        Parameters:
            name (str): Name of the person.

        Returns:
            list: Names of the person's grandchildren.
        """
        person = self.find_person(name)
        grandchildren = []
        for child_name in person.children: #find children of selected person
            child = self.find_person(child_name)
            if child:                       #check if we have info in database
                grandchildren.extend(child.children)
        return grandchildren                # return list of names

    def get_siblings(self, name):
        """
        Find the siblings of a person.

        Parameters:
            name (str): Name of the person.

        Returns:
            list: Names of the person's siblings.
    """
        parents = self.get_parents(name) # find parents
        siblings = set()                 #set --> no dublication
        for parent_name in parents:
            parent = self.find_person(parent_name)
            if parent:                    # Check if we have info in database
                siblings.update(parent.children)
        siblings.discard(name)              # Remove the person themselve
        return list(siblings)


    def get_cousins(self, name):
        """
        Find the cousins of a person.

        Parameters:
            name (str): Name of the person.

        Returns:
            list: Names of the person's cousins.
        """
        parents = self.get_parents(name) # find list of parents names
        cousins = []
        for parent_name in parents:
            parent = self.find_person(parent_name) # get all  info about parent
            if parent:                              # check if we have them in database
                for sibling_name in self.get_siblings(parent_name):
                    sibling = self.find_person(sibling_name) # get all info about parents siblings
                    if sibling:                         # check if we have them in database
                        cousins.extend(sibling.children) # add all sibling`s children  list
        return cousins

    def get_close_relatives(self, name):
        """
        Find the close relatives of a person.

        Parameters:
            name (str): The name of the person.

        Returns:
            dict: A dictionary containing lists of close relatives:
                - "parents": List of the person's parents.
                - "siblings": List of the person's siblings.
                - "spouse": List of the person's spouse.
                - "children": List of the person's children.

        Note:
            If the person is not found in the family tree, an empty dictionary is returned.
        """
        person = self.find_person(name)
        if not person:
            return {}
        return {
            "parents": person.parents,
            "siblings": self.get_siblings(name),
            "spouse": person.spouse,
            "children": person.children,
        }


    def get_extended_family(self, name):
        """
        Finds the extended family of a person (who are still alive)

        Parameters:
            name (str): The name of the person.

        Returns:
            dict:
                - "close_relatives": List of alive close relatives (parents, siblings, spouse, children).
                - "cousins": List of alive cousins.
                - "aunts_uncles": List of alive aunts and uncles.

        Note:
            - Relatives are included in the result only if they are alive.
            - If a person does not exist in the family tree, the method will return an empty dictionary.
        """

        close_relatives = self.get_close_relatives(name)
        extended_family = {
            "close_relatives": [],
            "cousins": [],
            "aunts_uncles": []
        }

        # filter close relatives
        for relation in close_relatives.values():
            for relative in relation:
                if self.is_alive(relative):
                    extended_family["close_relatives"].append(relative)

        # filter  cousins
        for cousin in self.get_cousins(name):
            if self.is_alive(cousin):
                extended_family["cousins"].append(cousin)

        # filter  aunts and uncles
        for aunt_uncle in self.get_aunts_uncles(name):
            if self.is_alive(aunt_uncle):
                extended_family["aunts_uncles"].append(aunt_uncle)

        return extended_family


    def get_aunts_uncles(self, name):
        """
        Finds the aunts and uncles of a person.

        Parameters:
            name (str): The name of the person.

        Returns:
            list: Names of the person's aunts and uncles.
        """
        parents = self.get_parents(name)                # get parents names
        aunts_uncles = []
        for parent_name in parents:                     # get all  info about parents
            parent = self.find_person(parent_name)
            if parent:                                  # check if we have them in database
                aunts_uncles.extend(self.get_siblings(parent_name))
        return aunts_uncles

    def is_alive(self, name):
        """
        Checks if a person has death date

        Parameters:
            name (str): Name of the person.

        Returns:
            bool: True if the person is alive, otherwise False.
        """

        person = self.find_person(name)
        return person and not person.death_date

# Provides family-wide statistics
class Statistics:
    def __init__(self, family_tree):
        self.family_tree = family_tree

    # find  the birthday for each person and returns a dictionary as the result (does not divide into paternal and maternal lines)
    def get_bdays(self):
        """
        Find the birthdays of all family members.

        Returns:
            dict: A dictionary mapping names to their birthdates .
        """
        birthdays = {}
        for name, person in self.family_tree.person.items():
            birthdays[name] = person.birth_date.strftime("%d-%m-%Y")
        return birthdays


    def get_bdays_calendar(self):
        """
        Find sorted birthdays calendar of all family members.

        Returns:
                dict: A dictionary mapping birthdates to family members names.
        """
        calendar = {}
        for name, person in self.family_tree.person.items():
            day_month = person.birth_date.strftime("%d-%m")
            if day_month not in calendar: #no day dublication
                calendar[day_month] = []
            calendar[day_month].append(name)
        sorted_calendar = dict(
            sorted(calendar.items(), key=lambda x: datetime.strptime(x[0], "%d-%m"))
            # sort by month
        )
        return sorted_calendar


    def get_children_count(self):
        """
        Find the number of children each person has.

        Returns:
        dict: A dictionary mapping names to their number of children.
        """

        children_count = {}
        for name, person in self.family_tree.person.items():
            children_count[name] = len(person.children)
        return children_count

    def get_average_children_pp(self):
        """
        Calculates the average number of children per person.

        Returns:
            int: The average number of children per person, rounded down.
        """
        children_count = self.get_children_count()
        total_children = sum(children_count.values())
        total_people = len(children_count)
        return total_children // total_people

    def get_average_age(self):
        """
        Calculates the average age of family members.

        Returns:
            int: The average age of family members, rounded down.
        """
        total_age = 0
        count = 0
        for person in self.family_tree.person.values():
            if person.death_date:
                # Calculate the age by subtracting the years
                age = person.death_date.year - person.birth_date.year
                # Adjust if the death date hasn't passed yet for the birthday in the current year
                if (person.death_date.month, person.death_date.day) < (person.birth_date.month, person.birth_date.day):
                    age -= 1
                total_age += age
                count += 1
        return total_age // count

def load_family_data():
    """
       Loads the family data into the system and initializes key components.

       This function creates a `FamilyTree` object from the provided `family_data`
       and a corresponding `Statistics` object for analyzing family-related metrics.

       Returns:
           tuple:
               - family_tree (FamilyTree)
               - statistics (Statistics)
    """
    family_tree = FamilyTree(family_data)
    statistics = Statistics(family_tree)
    return family_tree, statistics


# References:
# 1. Stack Overflow Discussions:https://stackoverflow.com/questions/63497433/python-how-do-i-extract-the-year-from-a-date
# 2. Python Tutorial : https://www.w3schools.com/python/
# 3. Python Documentation:https://docs.python.org/3/library/datetime.html



