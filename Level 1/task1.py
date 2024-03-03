#level 1 task 1 a string reverser
def reverse_string(input_string):
    return input_string[::-1]
input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)
