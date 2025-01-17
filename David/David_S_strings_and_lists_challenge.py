#David_S_strings_and_lists_challenge.py
# You run a startup media company called Ripple Media
# It's typical when you hire a new employee in your company, to setup an email id for them

employee_name = 'Ash Rahman'

# You have decided the format of the email should be: Ash Rahman -> ash.rahman@ripplemedia.com

# Let's write some code that converts a name into an email id that matches this format
print(employee_name.lower())
# 1.1 TODO: Let's save the lowercase version of the employee_name in a new variable 'lower_name' (use a string method to lower the name)
lower_name = employee_name.lower()
print(lower_name)
# 1.2 TODO: We want to separate the first name and last name and save it in a variable 'names_list' (use a string method to split the string into a list)
names_list = list(lower_name.split(' '))
print(names_list)
# 1.3 TODO: We want to join the first name and last name with a '.' and save it in a variable called 'joined_names' (use a string method to join the list into a new string)
names_list = ".".join(names_list)
print(names_list)
# 1.4 TODO: We want to add '@ripplemedia.com' to the end of the string inside joined_names and save it in a variable 'email' (use an f-string to combine the username with the email domain)
email = names_list + "@ripllemedia.com"
print(email)