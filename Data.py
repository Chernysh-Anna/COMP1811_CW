"""
Author: Anna Chernysh , Krishna Tamang
Date: 25.11.2024

Based on the requirements from the coursework, we created a module defines the `family_data` dictionary, which serves as the primary dataset
for representing the relationships and attributes of individuals in a family tree.
"""

family_data = {
    # M
    "Cornelia Emmersohn": {
        "birth_date": "12-05-1966",
        "death_date": None,
        "parents": ["Sita Devi", "Kiran Sharma"],
        "spouse": ["Otto Emmersohn"],
        "children": []
    },
    "Sita Devi": {
        "birth_date": "15-03-1920",
        "death_date": "10-10-1995",
        "parents": ["Lalita Devi", "Rajesh Kumar"],
        "spouse": ["Kiran Sharma"],
        "children": ["Cornelia Emmersohn", "Mira Sharma"]
    },
    "Kiran Sharma": {
        "birth_date": "20-06-1915",
        "death_date": "05-02-1998",
        "parents": ["Arjun Sharma", "Meera Sharma"],
        "spouse": ["Sita Devi"],
        "children": ["Cornelia Emmersohn", "Mira Sharma"]
    },
    "Mira Sharma": {
        "birth_date": "08-08-1948",
        "death_date": None,
        "parents": ["Sita Devi", "Kiran Sharma"],
        "spouse": ["Ajit Patel"],
        "children": []
    },
    "Arjun Sharma": {
        "birth_date": "08-08-1891",
        "death_date": "05-07-1950",
        "parents": [],
        "spouse": ["Meera Sharma"],
        "children": ["Kiran Sharma"]
    },
     "Meera Sharma": {
        "birth_date": "01-05-1895",
        "death_date": "13-07-1973",
        "parents": [],
        "spouse": ["Arjun Sharma"],
        "children": ["Kiran Sharma"]
    },

    "Ajit Patel": {
        "birth_date": "10-11-1945",
        "death_date": None,
        "parents": ["Anjali Patel", "Vikram Patel"],
        "spouse": ["Mira Sharma"],
        "children": []
    },
    "Lalita Devi": {
        "birth_date": "18-01-1885",
        "death_date": "23-04-1960",
        "parents": [],
        "spouse": ["Rajesh Kumar"],
        "children": ["Sita Devi", "Nina Devi"]
    },
    "Rajesh Kumar": {
        "birth_date": "14-02-1880",
        "death_date": "10-10-1955",
        "parents": [],
        "spouse": ["Lalita Devi"],
        "children": ["Sita Devi", "Nina Devi"]
    },
    "Nina Devi": {
        "birth_date": "21-12-1925",
        "death_date": None,
        "parents": ["Lalita Devi", "Rajesh Kumar"],
        "spouse": [],
        "children": ["Bob Devi"]
    },
    "Bob Devi": {
        "birth_date": "11-11-1969",
        "death_date": None,
        "parents": ["Nina Devi"],
        "spouse": [],
        "children": []
    },

    # Parental
    "Otto Emmersohn": {
        "birth_date": "28-01-1976",
        "death_date": None,
        "parents": ["Walter Emmersohn", "Anna Emmersohn"],
        "spouse": ["Cornelia Emmersohn"],
        "children": []
    },
    "Walter Emmersohn": {
        "birth_date": "25-06-1930",
        "death_date": "20-08-2000",
        "parents": ["Kevin Emmersohn", "Angela Halpert"],
        "spouse": ["Anna Emmersohn"],
        "children": ["Otto Emmersohn", "Lucy Emmersohn", "Alex Emmersohn"]
    },
    "Anna Emmersohn": {
        "birth_date": "19-12-1930",
        "death_date": "15-05-1997",
        "parents": ["Peter Scott", "Gloria May"],
        "children": ["Otto Emmersohn", "Lucy Emmersohn", "Alex Emmersohn"],
        "spouse": ["Walter Emmersohn"]
    },
    "Lucy Emmersohn": {
        "birth_date": "23-05-1978",
        "death_date": None,
        "parents": ["Walter Emmersohn", "Anna Emmersohn"],
        "spouse": ["Henry Issac"],
        "children": ["Steven Issac"]
    },
    "Eric Emmersohn": {
        "birth_date": "07-10-1980",
        "death_date": None,
        "parents": ["Walter Emmersohn", "Anna Emmersohn"],
        "spouse": ["Emma Jones"],
        "children": ["Jack Emmersohn"]
    },
    "Emma Jones": {
        "birth_date": "03-02-1982",
        "death_date": None,
        "parents": [],
        "spouse": ["Eric Emmersohn"],
        "children": ["Jack Emmersohn"]
    },
    "Jack Emmersohn": {
        "birth_date": "05-12-2009",
        "death_date": None,
        "parents": ["Eric Emmersohn","Emma Jones"],
        "spouse": [],
        "children": []
    },

    "Kevin Emmersohn": {
        "birth_date": "24-07-1894",
        "death_date": "08-04-1977",
        "parents": [],
        "spouse": ["Angela Halpert"],
        "children": ["Walter Emmersohn", "Ryan Emmersohn"]
    },
    "Angela Halpert": {
        "birth_date": "02-12-1896",
        "death_date": "05-02-1974",
        "parents": [],
        "children": ["Walter Emmersohn", "Ryan Emmersohn"],
        "spouse": ["Kevin Emmersohn"]
    },
    "Ryan Emmersohn": {
        "birth_date": "25-06-1930",
        "death_date": "07-03-2001",
        "parents": ["Kevin Emmersohn", "Angela Halpert"],
        "children": [],
        "spouse": [],
    },
    "Peter Scott": {
        "birth_date": "05-07-1893",
        "death_date": "04-12-1963",
        "parents": [],
        "spouse": ["Gloria May"],
        "children": ["Anna Scott"]
    },
    "Gloria May": {
        "birth_date": "25-12-1895",
        "death_date": "15-07-1963",
        "parents": [],
        "spouse": ["Peter Scott"],
        "children": ["Anna Scott"]
    }
}
