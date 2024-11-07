import tkinter as tk
from database import load_family_data

class FamilyTreeApp:
    def __init__(self, root):
        self.family_tree = load_family_data()
        self.root = root
        self.root.title("Генеалогічне дерево")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Ім'я:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)
        tk.Button(self.root, text="Показати батьків", command=self.show_parents).grid(row=1, column=0, columnspan=2)
        tk.Button(self.root, text="Показати онуків", command=self.show_grandchildren).grid(row=2, column=0, columnspan=2)
        tk.Button(self.root, text="Середній вік на момент смерті", command=self.show_average_age_at_death).grid(row=3, column=0, columnspan=2)

    def show_parents(self):
        name = self.name_entry.get()
        parents = self.family_tree.get_parents(name)
        if parents:
            self.display_result(f"Батьки {name}: {', '.join(parents)}")
        else:
            self.display_result(f"Батьків {name} не знайдено")

    def show_grandchildren(self):
        name = self.name_entry.get()
        grandchildren = self.family_tree.get_grandchildren(name)
        if grandchildren:
            self.display_result(f"Онуки {name}: {', '.join(grandchildren)}")
        else:
            self.display_result(f"Онуків {name} не знайдено")

    def show_average_age_at_death(self):
        average_age = calculate_average_age_at_death(self.family_tree)
        self.display_result(f"Середній вік на момент смерті: {average_age:.2f} років")

    def display_result(self, result):
        result_label = tk.Label(self.root, text=result)
        result_label.grid(row=4, column=0, columnspan=2)

# Інші методи для інтерфейсу...
