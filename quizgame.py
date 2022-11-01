print ("Welcome to my computer quiz!") 

playing = input("Do you want to play? ")

if playing.lower()  != "yes":
    quit()

print ("Okay, let's play")

score = 0

answer = input("WHat does CPU stand for? " ).lower()
if answer == "c":
    print("Correct!")
    score +=1
else:
    print("wrong")


answer = input("WHat does GPU stand for? " ) 
if answer.lower() == "g":
    print("Correct!")
    score +=1
else:
    print("wrong")


answer = input("WHat does RAM stand for? " ) 
if answer.lower() == "r":
    print("Correct!")
    score +=1
else:
    print("wrong")

print ("You got " + str(score) + " questions correct!")
print ("Which is " + str((score / 3) * 100) + "%")