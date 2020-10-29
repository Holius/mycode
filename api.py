#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
import math
from numpy.random import default_rng

def get_trending(facts): 
    upvote = -math.inf
    fact_text = ""
    for fact in facts: 
        if fact["upvotes"] > upvote:
            upvote = fact["upvotes"]
            fact_text = fact["text"]
    return [upvote, fact_text]

def get_random(facts):
    rng = default_rng()
    rand_int = rng.integers(0, len(facts))
    return facts[rand_int]["text"]

def get_choice():
    valid = {"a": True, "b": False}
    while True: 
        answer = input("a) trending b) random: ").lower()
        print(answer)
        if isinstance(valid.get(answer), bool):
            return valid[answer]
        print("select 'a' or 'b'")

    
def main():
    catfacts = requests.get('https://cat-fact.herokuapp.com/facts').json()["all"]
    disclaimer = "disclaimer: none of these facts are checked."
    choice = get_choice()
    if choice: 
        upvote, fact = get_trending(catfacts)
        print(f"the trending fact with {upvote} votes is this:\n{fact}\n{disclaimer}")
    else:
        print(f"{get_random(catfacts)}\n{disclaimer}") 


main()

