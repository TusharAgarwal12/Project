import random

# name of the story 

name = ["\t\t\t\t\t\tHunted night","\t\t\t\t\t\tHunted building","\t\t\t\t\t\tHunted trip","\t\t\t\t\t\tScary night"]


# list 


time = ["Once upon a time,","A couple of years ago,","Last year,","Last summer,","Last winter,"]    #1

persons = ["family","friends","family and friends"]                                             #2

place = ["mountains","Goa","Jammu and Kashmir"]                                                 #3

problem1 = ["their car breakdown.","a wild animal just jumped next to the car.","they see that a big tree was blocking their way as the car was unable to cross that."] #4

fifth5 = ["and noticed that there was nothing as of sight.","they noticed that there was not even a single living being.","it was dark all around."]               #5

sixth6 = ["the road was blocked,","there were a dead end and google was shoing directions,","the road was completely damaged by the land slide,"]                #6

hunted7 = ["church","house","banglow"]                                                         #7

oldhouse8 = ["100 years old.","200 years old.","500 years old."]                                  #8

ninth9 = ["came out of the car and","took their lugage","took the car near the building by pushing it"] #9

tenth10 = ["normal,","scary as it was from outside,"]                                                     #10

eleventh11 = ["some strange noice came.","the sound of children came.","a lot of bats came inside the building."] #11

twelve = ["a week.","two days.","three days.","five days."]                                                    #12 star 

thirteen = ["rainy night.","foggy night.","very dark night."]                                                  #13 dot


# choosing random values and assignig them to a part to use in the story



partone = random.choice(time)

parttwo = random.choice(persons)

partthree = random.choice(place)

partfour = random.choice(problem1)

partfive = random.choice(fifth5)

partsix = random.choice(sixth6)

partseven = random.choice(hunted7)

parteight= random.choice(oldhouse)

partnine = random.choice(ninth9)

partten = random.choice(tenth10)

parteleven = random.choice(eleventh11)

parttwelve = random.choice(twelve)       #star

partthirteen = random.choice(thirteen)      #dot

nameofthestory = random.choice(name)    #random name of the story

# the story begins here 

print('\n','\n',nameofthestory,'\n')

print(partone,"Rahul with his",parttwo,"planned for a trip of",parttwelve,"When they started, it was a",partthirteen,"They were going to",partthree,"from a short but very scary forest. In the middle of the forest Suddenly,",partfour,"They came out of the car",partfive,"They cleared the road and started their journey again, But after some time, covering a small distance in their way,",partsix,"But this time they saw a",partseven,"nearby which was looking",parteight,"They all decided to spend their night inside the building as it was a good shelter for that scary dark night. They all",partnine,"and went inside. \n \n The interior of the building was very",partten,"And their were no lights as it was a very old building. \n Thet all took out their clothes and tried to sleep in the hall of the building and suddenly,",parteleven," \n They understood that the building was not safe for the whole night as something was strange there. They all ran outside as fast as they could and came again in the morning to take their car out from there.\n \n That's how they were able to save their lives that night as the local people told them that it was a hunted building from last 100 years.\n \n")








# Here is the steps which we have implemented in the project.



#    The concepts of python which is used in our project.
#      1. concept of importing a module
#      2. concept of strings
#      3. concept of list 
#      4. concept of random function
#      5. concept of escape characters
#      6. concept of assignment operators


# Firstly we've imported Random Function because we were going to use it further in the code. 
# And then comes the name of the story we created a list of different names of the story and assigned them to a name variable.
# Then, In the next part we've created various lists of the situations which can be happen in the story and assigned them to different variables.

# Then comes the part of chossing the situations given in the lists. We've left that work on random function. The random function have given us random situations from the corresponding lists.

# Then comes the part of displaying the whole andom story and we've done that by the help of print function.
# And in last, We've displayed the whole story including the random situations chossen by the random function.



