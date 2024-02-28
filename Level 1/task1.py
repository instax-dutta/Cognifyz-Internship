#create a python function which takes a string as input and returns the reverse of it
def reverse_string(input_string):
    return input_string[::-1]
input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)
