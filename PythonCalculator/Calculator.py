'''
Python Calculator
Create by Marcos Vinicius
'''

operationMathematics = ('+', '-', '/', '*')
newOperationSplit = '$'


def printMenu():
    print("---PYTHON CALCULATOR---")
    print("Insert your mathematical operations")
    print("To close the calculator insert 'Exit'")


def inputExpression():
    return str(input("Expression: "))


def strTrim(string):
    return str(string).replace(" ", "")


def validListIsOnlyNumber(listNumber):
    result = True
    for element in listNumber:
        try:
            test = float(element)
        except ValueError:
            result = False
            break
    return result


def returnAllNumberExpression(string):
    expression = str(string)

    for operation in operationMathematics:
        expression = expression.replace(operation, newOperationSplit)

    listOnlyNumbers = expression.split(newOperationSplit)

    if validListIsOnlyNumber(listOnlyNumbers):
        return listOnlyNumbers
    else:
        return []


def calculate(allNumbersList, expressionString):
    result = float(allNumbersList[0])
    position = 1

    for characters in expressionString:
        if characters in operationMathematics:
            if characters == '+':
                result += float(allNumbersList[position])
            elif characters == '-':
                result -= float(allNumbersList[position])
            elif characters == '/':
                result /= float(allNumbersList[position])
            elif characters == '*':
                result *= float(allNumbersList[position])
            position += 1

    return float(result)


printMenu()
expression = inputExpression()
while (expression.upper() != 'Exit'.upper()):
    expression = strTrim(expression)
    allNumbersList = returnAllNumberExpression(expression)
    if len(allNumbersList) > 0:
        print("Result expresson: %.2f" % calculate(allNumbersList, expression))
    else:
        print("Expression Invalid!")

    printMenu()
    expression = inputExpression()
