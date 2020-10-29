#!bin/env python3

def is_number(string):
    try:
        result = float(string)
    except:
        return False
    return result


def get_input():
    operand1, operand2, operation = "","",""
    input_is_garbage = True
    operations = {"a":"add", "s":"subtract", "d":"divide", "m":"multiply"}

    while input_is_garbage:
        garbage = False
        if not is_number(operand1): 
            operand1 = input("Enter a number: ")
            if not is_number(operand1): garbage = True 
        if not is_number(operand2): 
            operand2 = input("Another one: ")
            if not is_number(operand2): garbage = True
        if not isinstance(operations.get(operation), str):
            operation = input("Enter (a) add, (s) substract, (d) divide, or (m) multiply: ").lower()
            if not isinstance(operations.get(operation), str): garbage = True
        input_is_garbage = garbage
        
    return [float(operand1), float(operand2), operations[operation]]

def calculate(state):
    if len(state) != 3 or not is_number(state[0]) or not is_number(state[1]) or not isinstance(state[2], str):
        return "Type Error or Not Enough Arguments in Calculate" 
    operand1, operand2, operation = state
    result = 0
    if operation == "add": result = operand1 + operand2
    elif operation == "subtract": result = operand1 - operand2
    elif operation == "divide": result = operand1 / operand2
    elif operation == "multiply": result = operand1 * operand2
    else: return "Operation not found."  
    return result if result != round(result) else int(result) 

answer = calculate(get_input())
print(answer)

#bonus
#import math
#def get_circumference(diameter):
#    if is_number(diameter): return calculate([float(diameter), math.pi, "multiply"])
#    return "Not a number"
    
#print(get_circumference(input("Diameter for circumference: ")))
