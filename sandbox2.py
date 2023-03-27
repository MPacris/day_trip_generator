restaurant_confirmation = input(f"Do you approve this {random_restaurant}---type 'OK' to confirm. ")  
    while restaurant_confirmation != 'OK':             
        random_restaurant = random.choice(restaurants)
        restaurant_confirmation = input(f"'Do you like your choice of {random_restaurant}---type 'OK' to confirm?  ")
       
    print(f"You have selected {random_restaurant} ")
   