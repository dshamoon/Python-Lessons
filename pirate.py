import random
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

#for question in questions:

# Gather user input
def pleasure():
    answersdictionry = {}
    print "choose Y or N"
    for question in questions:
        print questions[question] 
        answer = raw_input()    
        # print answer
        if answer == "Y" or answer == "y":
            answersdictionry[question] = True
        else: 
            answersdictionry[question] = False
    return answersdictionry


# Generate Drink ingredients
def hope(answersdictionry):
    print "This is our drink:"
    for phrase in answersdictionry:
        if answersdictionry[phrase] == True:
            print random.choice(ingredients[phrase])

# Build our drink.
# def drink(ingredients):
#     print "I hope you enjoy:"
#     for item in ingredients:
#         #for key, value in value.items():
#         if stuff.values() is True:
#             beverage.append(" something ")
#     return beverage
    


if __name__ == '__main__':
    hope(pleasure())

