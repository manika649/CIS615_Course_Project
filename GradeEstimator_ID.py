# Task: Grade Estimator
# Name: Manika Karki


# ---------- unit 1 -------- 

# Ask for name input
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

# String Cleaning (strip spaces and capitalize)
clean_first = first_name.strip().capitalize()
clean_last = last_name.strip().capitalize()


# ---------- unit 2 -------- 

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

# ---------- unit 3 -------- 

# Task: Unit 3 Grade Estimator
# Name: Manika Karki

# --- Step 1: Define Unit 1 Variables (From previous assignment) ---
Unit1_discussion_points = 50      # Points earned in Unit 1 discussion
Unit1_course_project_points = 50  # Points earned in Unit 1 project
Unit1_core_assessment_points = 50  # Points earned in Unit 1 core assessment

# --- Step 2: Define Unit 2 Variables (New entries/estimates) ---
Unit2_discussion_points = 45      # Points earned/estimated for Unit 2 discussion
Unit2_course_project_points = 48  # Points earned/estimated for Unit 2 project
Unit2_core_assessment_points = 0   # Placeholder if no core assessment in Unit 2

# --- Step 3: Create the 3 required lists using the variables above ---
# This list combines Unit 1 and Unit 2 discussion points
total_discussion_points = [Unit1_discussion_points, Unit2_discussion_points]
# This list combines Unit 1 and Unit 2 project points
total_course_project_points = [Unit1_course_project_points, Unit2_course_project_points]
# This list combines Unit 1 and Unit 2 core assessment points
total_core_assessment_points = [Unit1_core_assessment_points, Unit2_core_assessment_points]

# --- Step 4: Calculate Sums and Maximums ---
# Summing the values currently inside our lists
disc_sum = sum(total_discussion_points)
proj_sum = sum(total_course_project_points)
core_sum = sum(total_core_assessment_points)

# Max points logic: 8 tasks for disc/proj, 4 for core assessment (at 50 pts each)
max_disc = 8 * 50
max_proj = 8 * 50
max_core = 4 * 50

# --- Step 5: Display Results using String.format ---
# Displaying the discussion totals in the required format
print("Currently you have {0} points for discussions out of {1}".format(disc_sum, max_disc))
# Displaying the project totals in the required format
print("Currently you have {0} points for course projects out of {1}".format(proj_sum, max_proj))
# Displaying the core assessment totals in the required format
print("Currently you have {0} points for core assessments out of {1}".format(core_sum, max_core))


# ---------- unit 4 -------- 
# I updated the lists by using the Unit 1 variables I have already created. 
# # This replaces the Unit 2 estimates with my actual grades (50 and 45).
total_discussion_points = [Unit1_discussion_points, 50, 50] # Unit 2 actual: 50
total_course_project_points = [Unit1_course_project_points, 45, 45] # Unit 2 actual: 45
total_core_assessment_points = [Unit1_core_assessment_points, 0, 100] # Unit 2 actual: 0, as we didn't have core assessment for unit2
# 2. Define Classes to store homework rules (Required for Unit 4)
class Discussions:
    maximum_points_per_task = 50 # The max score for any discussion
    display_name = "discussion" # Used for the final output message
class Course_projects:
    maximum_points_per_task = 50 # The max score for any project
    display_name = "course project"

class Core_assesments:
    maximum_points_per_task = 100 # The max score for core assessments
    display_name = "core assessment"

# 3. Creating a function to check if I got maximum points (Required for Unit 4)
def check_performance(grades, assignment_type):
    # Set the variable to True to start (the "algorithm" requested)
    is_perfect = True 
    # Looping through the list of grades
    for score in grades: 
        # If any score is less than the max (including 0), set variable to False
        if score < assignment_type.maximum_points_per_task: 
            is_perfect = False 
    
    # Checking if the variable stayed True or became False
    if is_perfect:
        print(f"Congrats! You got maximum points for ALL {assignment_type.display_name} homeworks so far!")
    else:
        print(f"Unfortunately you did not get maximum points for ALL {assignment_type.display_name} homeworks")

# 4. Final Output for ID 1675569
print(f"\n--- Performance Report for ID: 1675569 ---")
# Calling the function for all three homework types
check_performance(total_discussion_points, Discussions)
check_performance(total_course_project_points, Course_projects)
check_performance(total_core_assessment_points, Core_assesments)
