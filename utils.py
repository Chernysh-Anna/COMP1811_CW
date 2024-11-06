from datetime import datetime

def calculate_average_age_at_death(family_tree):
    ages = []
    for person in family_tree.person.values():
        if person.death_date:
            age_at_death = (person.death_date - person.birth_date).days / 365.25
            ages.append(age_at_death)
    if ages:
        return sum(ages) / len(ages)
    return 0

def sort_birthdays(family_tree):
    birthdays = {}
    for person in family_tree.people.values():
        date_without_year = person.birth_date.strftime("%d-%m")
        if date_without_year not in birthdays:
            birthdays[date_without_year] = []
        birthdays[date_without_year].append(person.name)
    sorted_birthdays = dict(sorted(birthdays.items()))
    return sorted_birthdays

def count_children(family_tree):
    children_count = {}
    for person in family_tree.people.values():
        children_count[person.name] = len(person.children)
    return children_count

def average_children_count(family_tree):
    total_children = sum(len(person.children) for person in family_tree.people.values())
    return total_children / len(family_tree.people)
