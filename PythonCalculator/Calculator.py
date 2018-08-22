'''
Python Calculator
Create by Marcos Vinicius
'''

operationMathematics = ('+', '-', '/', '*')


def printMenu():
    print("---PYTHON CALCULATOR---")
    print("Insert your mathematical operations")
    print("To close the calculator inset 'Exit'")


def inputExpression():
    return str(input("Expression: "))


def removeSpaces(string):
    return str(string).replace(" ", "")


def returnOnlyNumber(listNubers):
    result = []
    for numbers in listNubers:
        if str(numbers).isdigit():
            result.append(float(numbers))
    return result


def returnAllNumberExpression(string):
    expression = str(string)
    listExpression = []

    for operation in operationMathematics:
        if operation in expression:
            listOnlyNumbers = returnOnlyNumber(expression.split(operation))
            for numbers in listOnlyNumbers:
                listExpression.append(numbers)

    return listExpression


def calculate(allNumbersList, expressionString):
    result = float(allNumbersList[0])
    position = 1

    for characters in expressionString:
        if characters in operationMathematics:
            if characters == '+':
                result += allNumbersList[position]
            elif characters == '-':
                result -= allNumbersList[position]
            elif characters == '/':
                result /= allNumbersList[position]
            elif characters == '*':
                result *= allNumbersList[position]
            position += 1

    return float(result)


printMenu()
expression = inputExpression()
while (expression.upper() != 'Exit'.upper()):
    expression = removeSpaces(expression)
    allNumbersList = returnAllNumberExpression(expression)
    result = calculate(allNumbersList, expression)
    print("Result expresson: %.2f" %result)

    printMenu()
    expression = imputExpression()
