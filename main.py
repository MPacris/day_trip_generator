#(5 points): As a developer, I want to make at least three commits with descriptive messages 

#(5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 
destinations = ['Amsterdam', 'Brussels', 'Stuttgart', 'Paris', 'Dublin']
restaurants = ['authentic local', 'chain international', 'grab and go', 'market food', 'eat in']
transportations = ['app ride share', 'public transportation', 'walk everywhere', 'personal driver','taxi']
entertainments = ['museum', 'zoo', 'walking tours', 'hop on hop off tours',  'sporting event', 'pub crawl', 'manufacturing tour', 'music event']

types_of_options = {destinations, restaurants, transportations, entertainments}

#(5 points): As a user, I want a destination to be randomly selected for my day trip. 
import random
random_destination = random.choice(destinations)
print(random_destination)

#(5 points): As a user, I want a restaurant to be randomly selected for my day trip

import random
random_restaurant = random.choice(restaurants)
print(random_restaurant)

#(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
import random
random_transportation = random.choice(transportations)
print(random_transportation)

#(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

import random
random_entertainment = random.choice(entertainments)
print(random_entertainment)





#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

confirmation = input("Do you approve of all of the choices?")
if confirmation == 'Yes':
    print('complete')
elif confirmation != 'Yes':
    for each_option in types_of_options:
        feedback = input("do you wish to keep this option?")
        



#(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
#(10  points): As a user, I want to display my completed trip in the console
#(5 points): Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing! 