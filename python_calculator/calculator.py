'''
Python Calculator
Create by Marcos Vinicius
'''

operation_mathematics = ('+', '-', '/', '*')
new_operation_split = '$'


def print_menu():
    print("---PYTHON CALCULATOR---")
    print("Insert your mathematical operations")
    print("To close the calculator insert 'Exit'")


def input_expression():
    return str(input("Expression: "))


def trim(string):
    return str(string).replace(" ", "")


def valid_list_only_number(list_numbers):
    result = True
    for element in list_numbers:
        try:
            test = float(element)
        except ValueError:
            result = False
            break
    return result


def return_all_number_expression(string):
    expression = str(string)

    for operation in operation_mathematics:
        expression = expression.replace(operation, new_operation_split)

    list_only_numbers = expression.split(new_operation_split)

    if valid_list_only_number(list_only_numbers):
        return list_only_numbers
    else:
        return []


def calculate(all_numbers_list, expression_string):
    result = float(all_numbers_list[0])
    position = 1

    for characters in expression_string:
        if characters in operation_mathematics:
            if characters == '+':
                result += float(all_numbers_list[position])
            elif characters == '-':
                result -= float(all_numbers_list[position])
            elif characters == '/':
                result /= float(all_numbers_list[position])
            elif characters == '*':
                result *= float(all_numbers_list[position])
            position += 1

    return float(result)


print_menu()
expression = input_expression()
while (expression.upper() != 'Exit'.upper()):
    expression = trim(expression)
    all_numbers_list = return_all_number_expression(expression)
    if len(all_numbers_list) > 0:
        print("Result expresson: %.2f" % calculate(all_numbers_list, expression))
    else:
        print("Expression Invalid!")

    print_menu()
    expression = input_expression()
