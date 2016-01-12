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

stuff = {
    'salty': True,
    'strong': True,
    'bitter': True,
    'fruity': True,
    'sweet': True
}  
#for question in questions:


def pleasure():
    answersdictionry = {}
    print "choose Y or N"
    for question in questions:
        print questions[question] 
        answer = raw_input()    
        if answer == "Y" or "y":
            answersdictionry[question] = True
        else: 
            answersdictionry[question] = False
    return answersdictionry

def hope():
    beverage = []
    for v in ingredients.values():
        beverage.append(random.choice(ingredients[v]))
    print beverage #random.choice(ingredients[v])
print hope()

# def drink():
#     beverage = []
#     for v in stuff.values():
#         #for key, value in value.items():
#         if stuff.values() is True:
#             beverage.append(" something ")
#     return beverage
#print drink()
    


#
# {'salty': False, 'strong': True, 'bitter': True, 'fruity': True, 'sweet': True}    

# # def what_yourpleasure():
# #     yourpleasure = {}
# #     for answer questions[]
# #     raw_input()
    
    
    
# # ##########

# # def mix_thedrink(yourpleasure):

# p1 = (random.choice(ingredients['strong']))
# p2 = (random.choice(ingredients['salty']))
# p3 = (random.choice(ingredients['bitter']))
# p4 = (random.choice(ingredients['sweet']))
# p5 = (random.choice(ingredients['fruity']))

# print "Answer Y or N"
# print questions['strong']
# a1  = raw_input()
# print questions['salty']
# a2  = raw_input()
# print questions['bitter']
# a3  = raw_input()
# print questions['sweet']
# a4  = raw_input()
# print questions['fruity']
# a5  = raw_input()


# if a1 == "Y":
#     print p1

# if a2 == "Y":
#     print p2

# if a3 == "Y":
#     print p3

# if a4 == "Y":
#     print p4

# if a5 == "Y":
#     print p5

    
     






# print "Your drink is a  " p1 , " " , p2 ," " , p3 ," " , p4 ," " , p5 ,



# for each question
# If Y, return a print 1 #questions['strong"]

#print questions['strong']


#for question, ingredient in questions.items():
#    print "%s You will get a \n \t %s" % (ingredient,question)
#print '-' * 10



#for questions, ingredient i :
#    print question



#print ingredients['strong']
#print random.choice(ingredients.keys())
#ingredients["strong".0]
# n = input("Enter Y or N: ")
# if N = "Y" print ingredients[strong]
#def drinks(questions,ingredients):
#    """this will just print out the questions and ingredients"""

# print("I'm  and I'm printing now".format(drinks(questions,ingredients).__name__))

#if __name__ == '__main__':
#   print drinks(questions,ingredients)
#for questions, print questions

