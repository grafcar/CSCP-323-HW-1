#check if value is a number
def isNum(value):
    if value == "1" or value == "2" or value == "3" or value == "4" or value == "5" or value == "6" or value == "7" or value == "8" or value == "9" or value == "0":       
        return True
    elif type(value) == int:
        return True
    elif type(value) == float:
        return True
    else:
        return False

#check if value is operand
def isOperand(value):
    if value == "*" or value == "+" or value == "-" or value == "/":
        return True
    else:
        return False

#removes ALL whitespaces, remove $, converts values into a list
def parsec(value):
    value = value.replace(" ","")
    value = value.replace("$","")
    list=[]
    list[:0]=value
    return list

#calculates x and y with the current operand, converts x and y from string to int when returning
def calculate(x,y, operand):
    if isNum(operand):
        return
    if operand == "*":
        return int(x)*int(y)
    elif operand == "-":
        return int(x)-int(y)
    elif operand == "+":
        return int(x)+int(y)
    elif operand == "/":
        return float(x)/float(y)
    else:
        print("There was an error with the calculation, please ensure the numbers and operands are correct") #if ends up with more number/operands than its counter part
        return 

#asks for input   
operation = input("Please enter your numbers and operators in postfix. When done enter $\n")

#if the input does not end in $ ask for the input again
while operation[len(operation)-1] != "$":
    operation = input("Remember to type $ at the end. Please enter your values again:\n")

#starting values
value = 0
operation = parsec(operation)
index = 0 
cont = True
result = True

#at the end of the calculation a question will be asked if cont, if input is 'y' then cont = true
while cont:
    #if the list of strings is less than 3, end loop
    while len(operation) >= 3:
        #if first 2 items of the list are numbers AND the third is an operand
        if isNum(operation[index]) and isNum(operation[index+1]) and isOperand(operation[index+2]):
            value = calculate(operation[index], operation[index+1], operation[index+2])
            operation = operation[:index] + operation[index+3:] #deletes the current 3 items of the index
            operation.insert(index,value) #inserts the new item on the index
            index = 0
        else:
            index += 1 #increment index value

    if result: print("Your result is: ", value)
    ans = input("Would you like to continue: y/n\n")
    if ans == "y":
        cont = True
        operation = input("Please enter your numbers and operators in postfix. When done enter $\n")

        while operation[len(operation)-1] != "$":
            operation = input("Remember to type $ at the end. Please enter your values again:\n")

        value = 0
        operation = parsec(operation)
        index = 0
        result = True
    elif ans == "n":
        cont = False
    else:
        result = False
        print("Please enter a valid character!")
