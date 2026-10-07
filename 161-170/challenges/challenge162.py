# Ask the user for a category and clean it so that 
# "FOOD", "Food", "fOod", "FoOd",  all becomes "food"


category = input("Category: ").strip().lower()
print("Cleaned category: ", category)
