# this is the different variables
boolean_variable = False
string_variable = "Hello world"
int_variable = 23
float_variable = 23.2

print(f"this is the different variables:\n boolean_variable: {boolean_variable} string_variable: {string_variable} "
      f"int_variable: {int_variable} float_variable:{float_variable}")

# we can know the type of variable with type() then we can cast using the cast func str(), int(), float(), bool()
print(type(float_variable))
print(float_variable)
new_variable_int = int(float_variable)
print(type(new_variable_int))
print(new_variable_int)

# we can get input from the user using the input func
new_string = input("Enter your name:\n")
print(f"Hello {new_string}")
