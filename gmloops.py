#!bin/env python3

def counter_one():
    forbidden = ["toy", "electronic", "book"]
    punishment = "watch Hallmark movies"
    location = "your room"
    for forbid in forbidden:
        print(f"For every {forbid} I find on the floor in {location}, that's how many times you will {punishment}.")

def delete_two():
    dollars = ["$","$", "$", "$","$"]
    lights = ["light1", "light2" , "light3"]
    print("For every light left on, I will remove a dollar from your piggy bank")
    for light in lights:
        dollars.pop()
    print(f"I only have {len(dollars)} dollars left")

def add_three():
     dollars = ["$","$", "$", "$","$"]
     dishes = ["dirty1", "dirty2", "dirty3"]
     print("For every dirty dish I found, I will add a dollar to your sibling's piggy bank")
     for dish in dishes:
         dollars.append("$")
     print(f"Your sibling now has {len(dollars)} dollars.")

counter_one()
print("---------------")
delete_two()
print("--------------")
add_three()
