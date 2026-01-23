# Use the input function to get the first name from the user
first_name = input("Please enter your first name: ") # Getting the first name input
# Use the input function to get the last name from the user
last_name = input("Please enter your last name: ") # Getting the last name input

# First, use .strip() to remove any accidental spaces before or after the names
first_stripped = first_name.strip() # Cleaning spaces from first name
last_stripped = last_name.strip()   # Cleaning spaces from last name

# Next, use .capitalize() to make the first letter big and others small
first_clean = first_stripped.capitalize() # Formatting first name casing
last_clean = last_stripped.capitalize()   # Formatting last name casing

# Use print to display the formatted greeting: Hello Last, First
print("Hello " + last_clean + ", " + first_clean) # Displaying the final greeting

# Create variables for the points earned for each task (setting all to 50)
Unit1_discussion_points = 50      # Points earned for the discussion
Unit1_course_project_points = 50  # Points earned for the course project
Unit1_core_assesment_points = 50  # Points earned for the core assessment

# Create a variable for the maximum points possible
task_maximum_points = 50          # This is the max limit variable

# Calculate the total points by adding the variables together
total_points = Unit1_discussion_points + Unit1_course_project_points + Unit1_core_assesment_points # Math logic
# Display the total points result
print("Total Points: " + str(total_points)) # Printing the total sum

# Compare my points to the max points variable to see if they are equal
# This will output 'True' because the values match
check_disc = Unit1_discussion_points == task_maximum_points # Comparison for discussion
print("Got maximum points for Unit 1 discussion? " + str(check_disc)) # Printing result

check_proj = Unit1_course_project_points == task_maximum_points # Comparison for project
print("Got maximum points for Unit 1 course project? " + str(check_proj)) # Printing result

check_core = Unit1_core_assesment_points == task_maximum_points # Comparison for assessment
print("Got maximum points for Unit 1 core assessment? " + str(check_core)) # Printing result


