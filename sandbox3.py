#(5 points): As a developer, I want to make at least three commits with descriptive messages 
#Commit 1, initial set up of file; 
#Commit 2, first pass of structure, minor updates; worked in sandbox
#Commit 3, move from sandbox2 to main.  updates as needed on wording for flow, removed extra imports and print functions

#(5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 
destinations = ['Amsterdam', 'Brussels', 'Stuttgart', 'Paris', 'Dublin']
restaurants = ['authentic local', 'international chain', 'grab and go', 'market', 'room service']
transportations = ['ride share app', 'public transportation', 'walking everywhere', 'personal driver','taxi']
entertainments = ['to a museum', 'to the zoo', 'on a walking tour', 'on a hop on hop off tour',  'to a sporting event', 'on a pub crawl', 'on a guided manufacturing tour', 'to a music event']



#(5 points): As a user, I want a destination to be randomly selected for my day trip. 
import random
random_destination = random.choice(destinations)

#(5 points): As a user, I want a restaurant to be randomly selected for my day trip

random_restaurant = random.choice(restaurants)

#(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 

random_transportation = random.choice(transportations)

#(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

random_entertainment = random.choice(entertainments)

#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.
print(f'The random day trip generator has suggested a day trip to {random_destination}, where you will eat {random_restaurant} food while exploring the city by {random_transportation} culminated by going {random_entertainment}!!!'  )


def confirm_choice(list, type):
    confirmation = ""
    while confirmation != 'OK':
        random_selection = random.choice(list)
        confirmation = input(f"The generator has selected {random_selection} for the {type} --- to confirm and lock in this selection type 'OK'!!  ")
    return confirmation


#(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
confirmation = input("To approve the randomly selected trip --type 'OK' !   ")
if confirmation == 'OK':
    print(f'Complete! Your trip to {random_destination}, where you will be eating {random_restaurant} food, while navigating the city by {random_transportation} and enjoying a trip to {random_entertainment} has been confirmed!!! ')

elif confirmation != 'OK':
    while confirmation != 'OK':
        
        confirmation = confirm_choice(destinations, 'destination')       
    print(f"You have selected {} as the destination city!")

    restaurant_confirmation = input(f"The generator has selected {random_restaurant} food for the suggestion for types of food --- to confirm and lock in this selection type 'OK' to confirm. ")  
    while restaurant_confirmation != 'OK':             
            random_restaurant = random.choice(restaurants)
            restaurant_confirmation = input(f"The generator has selected {random_restaurant} food for the suggestion for types of food --- to confirm and lock in this selection type 'OK' to confirm. ")
    print(f"You have selected {random_restaurant} as the type of food you will eat!")
   
    
    transportation_confirmation = input(f"The generator has selected {random_transportation} as the mode of mode of transportation to be used the city---type 'OK' to confirm  ")
    while transportation_confirmation != 'OK':
            random_transportation = random.choice(transportations)
            transportation_confirmation = input(f"The generator has selected {random_transportation} as the mode of mode of transportation to be used the city---type 'OK' to confirm  ")
    print(f"You have chosen {random_transportation} as the means for exploring the city!")

    entertainment_confirmation = input(f"The generator has selected for you to go {random_entertainment} as the chosen activity for entertainment---type 'OK' to confirm  ")
    while entertainment_confirmation != 'OK':
            random_entertainment = random.choice(entertainments)
            entertainment_confirmation = input(f"The generator has selected for you to go {random_entertainment} as the chosen activity for entertainment---type 'OK' to confirm  ")
    print(f"You have chosen to go {random_entertainment} as your entertainment activity")
#(10  points): As a user, I want to display my completed trip in the console

    print(f'Based on your locked in selections, the trip generator has you going to {random_destination}, eating {random_restaurant} food, while navigating the city by {random_transportation} and enjoying a trip to {random_entertainment}!!!!' )
        

#(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
    confirmation = input(f"If you are satisfied with your planned trip please type 'OK'  ")
    print(f"Complete! Your trip to {random_destination}, where you will be eating {random_restaurant} food, while navigating the city by {random_transportation} and enjoying a trip to {random_entertainment} has been confirmed!!! ")



#(5 points): Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!  