# 1. Create the collection (a Dictionary)
# I use curly braces {} for dictionaries
presidents = {
    "Bill Clinton": {"year": 1993, "terms": 2},
    "George W. Bush": {"year": 2001, "terms": 2},
    "Barack Obama": {"year": 2009, "terms": 2},
    "Donald Trump": {"year": 2017, "terms": 1},
    "Joe Biden": {"year": 2021, "terms": 1},
    "Student 1675569": {"year": 1675569, "terms": 2}  # This is me!
}
# 2. How to check info for Donald Trump
# We 'dig' into the dictionary using the keys
trump_year = presidents["Donald Trump"]["year"]
trump_terms = presidents["Donald Trump"]["terms"]
print("Donald Trump", trump_year, trump_terms, "term")
# 3. How to check info for ME
my_year = presidents["Student 1675569"]["year"]
my_terms = presidents["Student 1675569"]["terms"]
print("Student 1675569", my_year, my_terms, "terms")