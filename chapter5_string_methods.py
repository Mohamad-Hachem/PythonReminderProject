# this is some good usable string methods
name = input("Enter your name")
# len() method will return the length of the string
print(f"this is the length of your name {len(name)}")
# the .find() methode will help you find the first occurrence of a string inside a string index start from 0
print(f"this is where the first o occurs {name.find('o')}")
# the .find() methode will help you find the last occurrence of a string inside a string index start from 0
print(f"this is where the last o occurs {name.rfind('o')}")
# capitalize() would make the first letter upper
print(f"this is your name {name.capitalize()}")
# upper() would make the all letter upper
print(f"this is your name {name.upper()}")
# lower() would make the all letter lower
print(f"this is your name {name.lower()}")
# .isdigit() will check if every character is a digit
print("all is numbers" if name.isdigit() else "not all is number")
# .isalpha() will check if every character is a letter
print("all is letters" if name.isalpha() else "not all is letter")
# .count() will check how many string in the current string
print(f"this is how many there is of a in mohamad {name.count('a')}")
# .replace() will replace all first string with the second
print("Helloworld".replace("o", "I am pranking you".upper()))
# you can always use print(help(str)) to get all the needed functions that works with strings

# string indexing [start : end : step]
random_number = "123-213-321"
print(random_number[0:])
print(random_number[:4])
print(random_number[::2])
print(random_number[::-1])