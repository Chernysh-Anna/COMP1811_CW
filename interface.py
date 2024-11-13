
import tkinter as tk
from tkinter import ttk
from database import load_family_data


class AppInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Family Tree App")
        self.root.geometry("600x600")  # need to find correct size/ask
        self.family_tree, self.statistics = load_family_data()  #how to transfer separetly if needed
        self.create_widgets()

    def create_widgets(self):
        # Create Labels, Buttons, and other widgets
        self.title_label = tk.Label(self.root, text="Family Tree and Statistics", font=("Helvetica", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # ComboBox to select a person from the family tree
        self.person_label = tk.Label(self.root, text="Select a person:")
        self.person_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.person_names = list(self.family_tree.person.keys())  # List of all person names
        self.person_combobox = ttk.Combobox(self.root, values=self.person_names, state="readonly")
        self.person_combobox.grid(row=1, column=1, pady=5)
        self.person_combobox.set(self.person_names[0])  # Set the first person as default

        # Buttons for various functionalities
        self.bdays_button = tk.Button(self.root, text="Show Birthdays", command=self.show_bdays)
        self.bdays_button.grid(row=2, column=0, pady=10)

        self.bday_calendar_button = tk.Button(self.root, text="Show Birthday Calendar", command=self.show_bday_calendar)
        self.bday_calendar_button.grid(row=2, column=1, pady=10)

        self.siblings_button = tk.Button(self.root, text="Show Siblings", command=self.show_siblings)
        self.siblings_button.grid(row=3, column=0, pady=10)

        self.cousins_button = tk.Button(self.root, text="Show Cousins", command=self.show_cousins)
        self.cousins_button.grid(row=3, column=1, pady=10)

        self.parents_button = tk.Button(self.root, text="Show Parents", command=self.show_parents)
        self.parents_button.grid(row=4, column=0, pady=10)

        self.grandchildren_button = tk.Button(self.root, text="Show Grandchildren", command=self.show_grandchildren)
        self.grandchildren_button.grid(row=4, column=1, pady=10)

        self.immediate_family_button = tk.Button(self.root, text="Show Immediate Family",
                                                 command=self.show_immediate_family)
        self.immediate_family_button.grid(row=5, column=0, pady=10)

        self.extended_family_button = tk.Button(self.root, text="Show Extended Family",
                                                command=self.show_extended_family)
        self.extended_family_button.grid(row=5, column=1, pady=10)

        self.avg_age_button = tk.Button(self.root, text="Average Age at Death", command=self.show_avg_age)
        self.avg_age_button.grid(row=6, column=0, pady=10)

        self.children_count_button = tk.Button(self.root, text="Children Count", command=self.show_children_count)
        self.children_count_button.grid(row=6, column=1, pady=10)

        self.avg_children_button = tk.Button(self.root, text="Avg. Children per Person", command=self.show_avg_children)
        self.avg_children_button.grid(row=7, column=0, pady=10)

        # Text box to display answers
        self.result_text = tk.Text(self.root, width=70, height=10, wrap=tk.WORD)
        self.result_text.grid(row=8, column=0, columnspan=2, pady=20)
        self.result_text.config(state=tk.DISABLED)  # Initially, make it read-only

    def display_result(self, result):
        # Display result in the Text widget
        self.result_text.config(state=tk.NORMAL)  # Make it editable to insert text
        self.result_text.delete(1.0, tk.END)  # Clear previous content
        self.result_text.insert(tk.END, result)  # Insert new result
        self.result_text.config(state=tk.DISABLED)  # Make it read-only again

    # 1. Show Siblings
    def show_siblings(self):
        person_name = self.person_combobox.get()  # Get selected person
        siblings = self.family_tree.get_siblings(person_name)
        if siblings:
            self.display_result(f"Siblings of {person_name}: {', '.join(siblings)}")
        else:
            self.display_result(f"{person_name} has no recorded siblings.")

    # 2. Show Cousins
    def show_cousins(self):
        person_name = self.person_combobox.get()  # Get selected person
        cousins = self.family_tree.get_cousins(person_name)
        if cousins:
            self.display_result(f"Cousins of {person_name}: {', '.join(cousins)}")
        else:
            self.display_result(f"{person_name} has no recorded cousins.")

    # 3. Show Birthdays
    def show_bdays(self):
        birthdays = self.statistics.get_bdays()
        formatted_bdays = "\n".join([f"{name}: {date}" for name, date in birthdays.items()])
        self.display_result(f"Family Birthdays:\n{formatted_bdays}")

    # 4. Show Birthday Calendar
    def show_bday_calendar(self):
        bday_calendar = self.statistics.get_bdays_calendar()
        formatted_calendar = "\n".join([f"{date}: {', '.join(names)}" for date, names in bday_calendar.items()])
        self.display_result(f"Birthday Calendar:\n{formatted_calendar}")

    # 5. Show Parents
    def show_parents(self):
        person_name = self.person_combobox.get()  # Get selected person
        parents = self.family_tree.get_parents(person_name)
        if parents:
            self.display_result(f"Parents of {person_name}: {', '.join(parents)}")
        else:
            self.display_result(f"{person_name} has no recorded parents.")

    # 6. Show Grandchildren
    def show_grandchildren(self):
        person_name = self.person_combobox.get()  # Get selected person
        grandchildren = self.family_tree.get_grandchildren(person_name)
        if grandchildren:
            self.display_result(f"Grandchildren of {person_name}: {', '.join(grandchildren)}")
        else:
            self.display_result(f"{person_name} has no recorded grandchildren.")

    # 7. Show Immediate Family
    def show_immediate_family(self):
        person_name = self.person_combobox.get()  # Get selected person
        relatives = self.family_tree.get_close_relatives(person_name)
        formatted_relatives = "\n".join(
            [f"{relation.capitalize()}: {', '.join(names)}" for relation, names in relatives.items()])
        self.display_result(f"Immediate Family of {person_name}:\n{formatted_relatives}")

    # 8. Show Extended Family
    def show_extended_family(self):
        person_name = self.person_combobox.get()  # Get selected person
        extended_family = self.family_tree.get_extended_family(person_name)
        if extended_family:
            self.display_result(f"Extended family of {person_name}: {', '.join(extended_family)}")
        else:
            self.display_result(f"Extended family of {person_name} is not available.")

    # 9. Show Average Age at Death
    def show_avg_age(self):
        avg_age = self.statistics.get_average_age()
        self.display_result(f"Average age at death: {avg_age} years")

    # 10. Show Children Count
    def show_children_count(self):
        children_count = self.statistics.get_children_count()
        formatted_count = "\n".join([f"{name}: {count}" for name, count in children_count.items()])
        self.display_result(f"Children Count for each person:\n{formatted_count}")

    # 11. Show Average Children per Person
    def show_avg_children(self):
        avg_children = self.statistics.get_average_children_pp()
        self.display_result(f"Average children per person: {avg_children}")



