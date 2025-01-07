"""
Author: Anna Chernysh , Krishna Tamang
Date: 25.11.2024

This module implements a Tkinter-based graphical user interface (GUI) for interacting
with a family tree system.

Key Features:
    - Person Selection: a combobox to select individuals from the family tree.
    - Relationship Data: buttons  display parents, siblings, grandchildren, cousins,
      ,immediate and extended family.
    - Statistical Data: buttons to view birthdays, birthday calendars, average age at death, average children per person
      and children counts.
    - Results Display: A text box to display results.
"""

import tkinter as tk
from tkinter import ttk
from Database import load_family_data

class AppInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Family Tree App")
        self.root.geometry("600x600")  # need to find correct size/ask
        self.root.config(bg="light blue")
        self.family_tree, self.statistics = load_family_data()
        self.create_widgets()

    # arrangement using a grid
    # ----------------------
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Welcome to Family Tree App", font=( 16),bg="light blue").grid(row=0, column=0, columnspan=2, pady=10)

# ComboBox to select a person from the family tree
        self.person_label = tk.Label(self.root, text="Select a person:", font=(6),bg="light blue").grid(row=1, column=0, pady=5,columnspan=2)


        self.person_names = list(self.family_tree.person.keys())  # List of all person names
        self.person_combobox = ttk.Combobox(self.root, values=self.person_names, state="readonly")
        self.person_combobox.grid(row=1, column=1, pady=5)
        self.person_combobox.set(self.person_names[0])  #  default person

        self.s_data_label = tk.Label(self.root, text="Statistic data:",bg="light blue").grid(row=2, column=0, columnspan=1, pady=5)

        button_style = {"bg":"peach puff"}

        self.parents_button = tk.Button(self.root, text="Show Parents", command=self.show_parents, **button_style)
        self.parents_button.grid(row=2, column=1, pady=10)

        self.bdays_button = tk.Button(self.root, text="Show Birthdays", command=self.show_bdays, **button_style)
        self.bdays_button.grid(row=3, column=0, pady=10)

        self.siblings_button = tk.Button(self.root, text="Show Siblings", command=self.show_siblings, **button_style)
        self.siblings_button.grid(row=3, column=1, pady=10)

        self.bday_calendar_button = tk.Button(self.root, text="Show Birthday Calendar", command=self.show_bday_calendar, **button_style)
        self.bday_calendar_button.grid(row=4, column=0, pady=10)

        self.grandchildren_button = tk.Button(self.root, text="Show Grandchildren", command=self.show_grandchildren, **button_style)
        self.grandchildren_button.grid(row=4, column=1, pady=10)

        self.children_count_button = tk.Button(self.root, text="Children Count", command=self.show_children_count, **button_style)
        self.children_count_button.grid(row=5, column=0, pady=10)


        self.cousins_button = tk.Button(self.root, text="Show Cousins", command=self.show_cousins, **button_style)
        self.cousins_button.grid(row=5, column=1, pady=10)

        self.avg_children_button = tk.Button(self.root, text="Avg. Children per Person", command=self.show_avg_children, **button_style)
        self.avg_children_button.grid(row=6, column=0, pady=10)


        self.extended_family_button = tk.Button(self.root, text="Show Extended Family",
                                                command=self.show_extended_family, **button_style)
        self.extended_family_button.grid(row=6, column=1, pady=10)

        self.avg_children_button = tk.Button(self.root, text="Avg. Children per Person", command=self.show_avg_children, **button_style)
        self.avg_children_button.grid(row=6, column=0, pady=10)

        self.avg_age_button = tk.Button(self.root, text="Average Age at Death", command=self.show_avg_age, **button_style)
        self.avg_age_button.grid(row=7, column=0, pady=10)

        self.immediate_family_button = tk.Button(self.root, text="Show Immediate Family",
                                                 command=self.show_immediate_family, **button_style)
        self.immediate_family_button.grid(row=7, column=1, pady=10)

# Text box for answers
        self.result_text = tk.Text(self.root, width=70, height=10, wrap=tk.WORD)
        self.result_text.grid(row=8, column=0, columnspan=2, pady=20, padx=20)
        self.result_text.config(state=tk.DISABLED)  #  make it read-only
#------------

# Display result
    def display_result(self, result):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)  # Clear previous answer
        self.result_text.insert(tk.END, result)  # Insert new result
        self.result_text.config(state=tk.DISABLED)
        # 5. Show Parents

# f1a(i) Show parents
    def show_parents(self):
        person_name = self.person_combobox.get()  # Get selected person
        parents = self.family_tree.get_parents(person_name)
        if parents:
            self.display_result(f"Parents of {person_name}: {', '.join(parents)}")
        else:
            self.display_result(f"{person_name} has no recorded parents.")

 # f1a(ii) Show Grandchildren
    def show_grandchildren(self):
        person_name = self.person_combobox.get()
        grandchildren = self.family_tree.get_grandchildren(person_name)
        if grandchildren:
            self.display_result(f"Grandchildren of {person_name}: {', '.join(grandchildren)}")
        else:
            self.display_result(f"{person_name} has no recorded grandchildren.")

# f1b(i) Show Immediate Family
    def show_immediate_family(self):
        person_name = self.person_combobox.get()  # Get selected person
        relatives = self.family_tree.get_close_relatives(person_name)
        formatted_relatives = "\n".join(
            [f"{relation.capitalize()}: {', '.join(names)}" for relation, names in relatives.items()])
        self.display_result(f"Immediate Family of {person_name}:\n{formatted_relatives}")

# f1b(ii) Show Extended Family
    def show_extended_family(self):
        person_name = self.person_combobox.get()
        relatives = self.family_tree.get_extended_family(person_name)
        formatted_relatives = "\n".join(
            [f"{relation.capitalize()}: {', '.join(names)}" for relation, names in relatives.items()])
        self.display_result(f"Extended Family of {person_name}:\n{formatted_relatives}")

# f2a(i) Show Siblings
    def show_siblings(self):
        person_name = self.person_combobox.get()
        siblings = self.family_tree.get_siblings(person_name)
        if siblings:
            self.display_result(f"Siblings of {person_name}: {', '.join(siblings)}")
        else:
            self.display_result(f"{person_name} has no recorded siblings.")

# f2a(ii) Show Cousins
    def show_cousins(self):
        person_name = self.person_combobox.get()
        cousins = self.family_tree.get_cousins(person_name)
        if cousins:
            self.display_result(f"Cousins of {person_name}: {', '.join(cousins)}")
        else:
            self.display_result(f"{person_name} has no recorded cousins.")

# f2b(i) Show Birthdays
    def show_bdays(self):
        birthdays = self.statistics.get_bdays()
        formatted_bdays = "\n".join([f"{name}: {date}" for name, date in birthdays.items()])
        self.display_result(f"Family Birthdays:\n{formatted_bdays}")

# f2b(ii) Show Birthday Calendar
    def show_bday_calendar(self):
        bday_calendar = self.statistics.get_bdays_calendar()
        formatted_calendar = "\n".join([f"{date}: {', '.join(names)}" for date, names in bday_calendar.items()])
        self.display_result(f"Birthday Calendar:\n{formatted_calendar}")

# f3a (iii) Show Average Age at Death
    def show_avg_age(self):
        age = self.statistics.get_average_age()
        self.display_result(f"Average age at death: {age} years")

# f3b (i) Show Children Count
    def show_children_count(self):
        children_count = self.statistics.get_children_count()
        formatted_count = "\n".join([f"{name}: {count}" for name, count in children_count.items()])
        self.display_result(f"Children Count for each person:\n{formatted_count}")

# f3b (ii) Show Average Children per Person
    def show_avg_children(self):
        avg_children = self.statistics.get_average_children_pp()
        self.display_result(f"Average children per person: {avg_children}")



