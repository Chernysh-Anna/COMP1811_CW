from family_data import family_data    #so we get actual data and not just module
from models import FamilyTree, Statistics

def load_family_data():
    family_tree = FamilyTree(family_data)
    statistics = Statistics(family_tree)
    return family_tree, statistics


