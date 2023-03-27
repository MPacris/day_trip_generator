#(5 points): As a developer, I want to make at least three commits with descriptive messages 

#(5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 
destinations = ['Amsterdam', 'Brussels', 'Stuttgart', 'Paris', 'Dublin']
restaurants = ['authentic local', 'chain international', 'grab and go', 'market food', 'eat in']
transportations = ['app ride share', 'public transportation', 'walk everywhere', 'personal driver','taxi']
entertainments = ['museum', 'zoo', 'walking tours', 'hop on hop off tours',  'sporting event', 'pub crawl', 'manufacturing tour', 'music event']

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





#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

confirmation = input("Do you approve of all of the choices -- type 'Yes' or 'No'? ")
if confirmation == 'Yes':
    print('complete')

elif confirmation != 'Yes':
    
    destination_confirmation = input(f"Do you approve this {random_destination}---type 'OK' to confirm ")  
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
        transportation_confirmation = input(f"'Do you like your choice of {random_transportation}---type 'OK' to confirm  ")

    print(f"You have chosen {random_transportation}")

    entertainment_confirmation = input(f"Do you like your choice of {random_entertainment}---type 'OK' to confirm  ")
    while entertainment_confirmation != 'OK':
        random_entertainment = random.choice(entertainments)
        entertainment_confirmation = input(f"Do you like your choice of {random_entertainment}---type 'OK' to confirm  ")

    print(f"You have chosen {random_entertainment}")




    
    
          
                
    

