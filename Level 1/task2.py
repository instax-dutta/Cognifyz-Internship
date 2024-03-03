#level 1 task 2 a temperature converter
def convert_temp(temp, unit):
    if unit == 'C':
        return (temp * 9/5) + 32
    elif unit == 'F':
        return (temp - 32) * 5/9
    else:
        return 'Invalid unit'

temp = float(input('Enter temperature: '))
unit = input('Enter unit (C/F): ')

converted_temp = convert_temp(temp, unit)
print(f'{temp} {unit} = {converted_temp} F')
print(f'{converted_temp} F = {convert_temp(converted_temp, "F")} C')
print(f'{converted_temp} F = {convert_temp(converted_temp, "C")} F')
