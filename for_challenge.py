#!bin/env python3

#todo make dynamic input

limit = input("Enter a positive whole number! If you are dumb user, nothing will happen! ")
 
def build_pyramid(limit=5):
    if limit <= 0: return
    iterations = limit + ((limit -1) * 2)
    current = 1
    up = True
    for block in range(iterations):
        print("*" * current)
    
        if current == limit: up = False 
        current = current + 1 if up else current - 1

if limit.isnumeric():
    build_pyramid(int(limit))

