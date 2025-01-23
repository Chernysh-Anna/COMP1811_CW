# COMP1811_CW
# Family Tree and Statistics Management System

This project is a Python-based system for managing and analyzing family tree data. It includes classes to handle individual family members, their relationships, and various family-wide statistics.

## Features

- **FamilyTree Class**:
  - Manage relationships such as parents, children, siblings, and extended family members.
  - Identify family members' cousins, aunts, uncles, and grandchildren.
  - Determine if a family member is alive based on provided data.
  - Retrieve close and extended relatives who are alive.

- **Statistics Class**:
  - Calculate average age and number of children per person in the family.
  - Generate a birthday calendar for all family members.
  - Count the number of children each person has.

# FamilyTree and Statistics Project

## Overview
This project provides a comprehensive family tree management and analysis system. It consists of two main classes:

1. **FamilyTree**: Handles the creation and management of family relationships.
2. **Statistics**: Provides various statistical insights about the family.

## Features

### FamilyTree Class
- **Initialize Family Tree**: Create a family tree from given family data.
- **Find Person**: Retrieve a person's details by their name.
- **Get Parents**: Find the parents of a given person.
- **Get Grandchildren**: Retrieve the names of a person's grandchildren.
- **Get Siblings**: Find the siblings of a person.
- **Get Cousins**: Retrieve the names of a person's cousins.
- **Get Close Relatives**: Retrieve close family members including parents, siblings, spouse, and children.
- **Get Extended Family**: Retrieve extended family members who are alive, including close relatives, cousins, aunts, and uncles.
- **Get Aunts and Uncles**: Retrieve the names of a person's aunts and uncles.
- **Check if Alive**: Determine if a person is still alive based on the absence of a death date.

### Statistics Class
- **Get Birthdays**: Retrieve a dictionary mapping family members' names to their birthdates.
- **Get Birthday Calendar**: Retrieve a sorted dictionary of birthdates to names, providing a birthday calendar.
- **Get Children Count**: Retrieve the number of children each person has.
- **Get Average Children per Person**: Calculate the average number of children per person.
- **Get Average Age**: Calculate the average age of deceased family members.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/family-tree.git
   ```
2. Navigate to the project directory:
   ```bash
   cd family-tree
   ```
3. Install any necessary dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```


### Example Operations
- **Find a Person**:
  ```python
  person = family_tree.find_person("John Doe")
  ```
- **Get Parents**:
  ```python
  parents = family_tree.get_parents("John Doe")
  ```
- **Get Grandchildren**:
  ```python
  grandchildren = family_tree.get_grandchildren("Jane Doe")
  ```
- **Get Birthday Calendar**:
  ```python
  birthday_calendar = statistics.get_bdays_calendar()
  ```





