# Task: Grade Estimator
# Name: Manika Karki

# Ask for name input
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

# String Cleaning (strip spaces and capitalize)
clean_first = first_name.strip().capitalize()
clean_last = last_name.strip().capitalize()

# Math calculation (50 points per category)
disc_points = 50
proj_points = 50
core_points = 50
total_points = disc_points + proj_points + core_points

# Display Results
print(f"Hello {clean_last}, {clean_first}")
print(f"Total Points: {total_points}")

# Logic checks
print(f"Discussion points equal 50? {disc_points == 50}")
print(f"Project points equal 50? {proj_points == 50}")
print(f"Core points equal 50? {core_points == 50}")
