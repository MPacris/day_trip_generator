#(5 points): As a developer, I want to make at least three commits with descriptive messages 

#(5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 
destinations = ['Amsterdam', 'Brussels', 'Stuttgart', 'Paris', 'Dublin']
restaurants = ['authentic local', 'chain international', 'grab and go', 'market', 'room service']
transportations = ['app ride share', 'public transportation', 'walk everywhere', 'personal driver','taxi']
entertainments = ['to a museum', 'to the zoo', 'on walking tours', 'on hop on hop off tours',  'to a sporting event', 'on a pub crawl', 'on a guided manufacturing tour', 'to a music event']

types_of_options = (destinations, restaurants, transportations, entertainments)

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



#Adding in introductory sentence to tie in all for lists
print(f'The day trip planner has generated the following suggestion:  A day trip to {random_destination}, where you will eat {random_restaurant} types of food while exloring the city by {random_transportation} culminated by going {random_entertainment}!!!'  )

#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

confirmation = input("To approve the randomly selected trip --type 'OK' !   ")
if confirmation == 'OK':
    print('complete')

elif confirmation != 'OK':
    while confirmation != 'OK':
        destination_confirmation = input(f"Do you approve this {random_destination}---type 'OK' to confirm   ")  
        while destination_confirmation != 'OK':             
            random_destination = random.choice(destinations)
            destination_confirmation = input(f"Do you like your choice of {random_destination}---type 'OK' to confirm  ")
        print(f"You have selected {random_destination} ")

        restaurant_confirmation = input(f"Do you approve this {random_restaurant}---type 'OK' to confirm. ")  
        while restaurant_confirmation != 'OK':             
            random_restaurant = random.choice(restaurants)
            restaurant_confirmation = input(f"Do you like your choice of {random_restaurant}---type 'OK' to confirm  ")
        print(f"You have selected {random_restaurant} ")
   
    
        transportation_confirmation = input(f"Do you like your choice of {random_transportation}---type 'OK' to confirm  ")
        while transportation_confirmation != 'OK':
            random_transportation = random.choice(transportations)
            transportation_confirmation = input(f"Do you like your choice of {random_transportation}---type 'OK' to confirm  ")
        print(f"You have chosen {random_transportation}")

        entertainment_confirmation = input(f"Do you like your choice of {random_entertainment}---type 'OK' to confirm  ")
        while entertainment_confirmation != 'OK':
            random_entertainment = random.choice(entertainments)
            entertainment_confirmation = input(f"Do you like your choice of {random_entertainment}---type 'OK' to confirm  ")
        print(f"You have chosen {random_entertainment}")

        print(f'Based on your locked in selections, the trip planned has you going to {random_destination}, eating {random_restaurant} food, while navigating the city by {random_transportation} and enjoying a trip to {random_entertainment}!!!!' )
        confirmation = input(f"If you are satisfied with your planned trip please type 'OK'  ")

    print("Complete!")




    
    
          
                
    

