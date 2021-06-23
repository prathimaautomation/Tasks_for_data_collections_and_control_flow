# Version 1 specs - with concatenation
#define a variable `name`, and assign a string
name = "park"
#re assign the original variable with your name
name = "    prathima "
#use concatenation to print a welcome message and use methods to format the name/input (remove white spaces)
print("Welcome to Sparta Global " + name.strip() + "!")

# Version 2 - with interpolation
# define another variable `full_name` to a random string
full_name = "garden"
# re assign the variable `full_name` to a name
full_name = "Diana"

# use interpolation to print the message
print(f'{full_name}! Welcome to the DevOps World.')
print('%s! Welcome to the DevOps World.'%(full_name))
print('{}! Welcome to the DevOps World.'.format(full_name))

### Refactor the code!

# The variables should never have trailing empty spaces
print("Welcome to Sparta Global " + name.strip() + "!")
print('{}! Welcome to DevOps World.'.format(full_name.strip()))

# The variables should always have the first letter capitalized
print("Welcome to Sparta Global " + name.strip().capitalize() + "!")
# we should be able to input several names and all have the first letter capitalized
print(input("Enter a name with first letter in lowercase please: ").capitalize())

## Acceptance Criteria
# The program defines the variables `name` and `full_name`
# The program re assinged variables `name` and `full_name`
# The program capitalizes names
# The program outputs a welcome message
