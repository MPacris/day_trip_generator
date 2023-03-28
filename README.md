# day_trip_generator

Setup Steps
Create a GitHub repository on GitHub. Remember to use a Python .gitignore and add a README!
    #completed

Clone your repository down to your computer (referring to the Code Demo – Source Control video would be helpful here!) 
    #completed
Create your project in Visual Studio Code and move the invisible .git folder and README file to the folder where your project is located.
    #completed
Make a test commit and check your repository to be sure the content has been updated!
    #completed

Start coding the program first by going from the top of the user stories and working down. Decide how you will:


Store the trip options for destinations, restaurants, transportation, and entertainment each in their own List (this would be good to place at the top of the file)
    #lists are defined at the top
    #followed by random selections

Get a random element from each of those sets of options. We recommend declaring variables for a random destination, restaurant, transportation, and entertainment

Display the initial random trip to your user
#displayed the initial trip in sentence form plugging in the initial randomly generated xchoices to be confirmed

Prompt the user to see if they are satisfied 
#there are two main confirmation steps. 1st where initial options are given, 2nd when options are locked in and other randomly generated.

#if user does not OK first set of choices, then the 4 lists are reviewed one at a time where they get to choose if they want to keep the initial suggestion.



(5 points): As a developer, I want to make at least three commits with descriptive messages 
    #1st one created duriing set up.  Be sure to capture changes in the message
    #2nd one had basic structure and flow
    #3rd one is more aesthetically sound and limited redundance.  To look to see if more can be condensed..

(5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 
    # there will be 4 total lists at the top


(5 points): As a user, I want a destination to be randomly selected for my day trip. 
(5 points): As a user, I want a restaurant to be randomly selected for my day trip
(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
    #Created lists so that they are generic and worded in a manner that no list is dependent on another list.  All outcomes can be interchangeable


(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.
    #My initial thought was to do an initial conditional, then go to for loops if first question is not true
    #After getting stuck, on for loops, I went back through handbook and have gone with initial, if else, then to separate while loops
    #while loops prompt random new random choice to be confirmed until 'OK' then moves on 

(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
    #if initial randomly generated list is apporved, then have it goto mark complete.  If initial question does not pass then it will go through while loops, then once all are confirmed mark entire trip complete.  will use input function for user confirmations where OK is needed to move forward
    

(10  points): As a user, I want to display my completed trip in the console
    #have marked complete as final steps


(5 points): Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing! 