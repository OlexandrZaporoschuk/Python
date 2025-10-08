user_answers = ["Yes", "", "No", "", "Maybe", "", "Yes"]

# Create a new list without empty answers
# using filter with a lambda expression
new_user = list(filter(lambda x: if len(x) != 0: return x , user_answers))

# Display the cleaned list of answers
print(new_user)