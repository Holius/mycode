#acceptable = <type list> answer = <type str> returns <type str>
def validate_answer(acceptable, answer):
    answer = answer.lower()
    if answer in acceptable: return answer
    return "none"

stages = {
            "intro": ["Are you a horse?",{"no":"outro", "maybe": "leg_amount", "yes": "leg_amount"}], 
            "leg_amount": ["How many legs do you walk on?", {"two": "outro", "four": "really"}], 
            "really": ["Really?", {"no": "literacy", "yes": "literacy"}], 
            "literacy": ["Can you read and write?",{"yes": "outro", "no": "truth"}], 
            "truth": ["Liar, you're reading this.",{"yes": "outro"}], 
            "outro": ["You're not a hourse. Flowchart brought to you by fatalistic_flowcharts_llc."]
          }

def main():
    print("press 'q' to quit at any time")
    current = stages["intro"]
    while (len(current) == 2):
        question, answers = current
        answer = input(f"{question} ")
        if answer == "q": 
            return print("Goodbye Human or Horse")
        elif validate_answer(answers.keys(), answer) != "none": 
            #current[1][answer] = name/value of next stage to load
            current = stages[current[1][answer]]
        else: 
            print("Answer " + " or ".join(answers.keys()))
    print(current[0])

main()
