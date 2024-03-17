DIVIDER = "--------------------------------------------"
GREETING = "This is the beginning of this task! :)"

print(DIVIDER)
print(GREETING)
print(DIVIDER)  
# 1. The Range Riddle

# for i in range(5, 2):
#     print(i)

# Task 1:
for i in range(5, 2, -1):
    print(i)
    
    
# Task 2:
import random as r

moods=["happy", "sad", "energetic", "calm"]
days=["Monday", "Thusday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i in range(len(days)):
    print(f"{days[i]}: {r.choice(moods)}")
    
    
# Task 3:
for i in range(10, 0, -1):
    print(i)

print(DIVIDER)
print(GREETING)
print(DIVIDER)  
# 2. Double Scoop with Nested Loops

# for i in range(3):
#     for j in range(3):
#         print("*")
#     print("\\n")

# Task 1:
for i in range(3):
    print("***")
                
    
# Task 2:
hourday=["morning", "afternoon", "evening"]
for i in range(len(days)):
    for i in range(len(hourday)):
        print(f"{days[i]}-{hourday[i]}: {r.choice(moods)}")
        
# Task 3: 
for i in range(1,6):
    for n in range(1,6):
        print(i*n, end="  ")
    print('\n')
    
print(DIVIDER)
print(GREETING)
print(DIVIDER)  
# 3. Mastering Python's For Loop

# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)

# Task 1:
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
    
# Task 2:
hourday=["morning", "afternoon", "evening", "lunchtime"]
for i in range(len(days)):
    for i in range(len(hourday)):
        if hourday[i]=="lunchtime":
            continue
        print(f"{days[i]}-{hourday[i]}: {r.choice(moods)}")


# Task 3: 
numbers=[1,2,3,3,5,6]

for i in numbers:
    if i==4:
        four=False
        break
    else:
        four=True    
            
if four:
    print("4 Not Found")

print(DIVIDER)
print(GREETING)
print(DIVIDER)  
# 4. The Marshmallow Increment Challenge

marshmallows = 0
while marshmallows < 5:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")



# Task 1:

# My predict is that it is going to print five times the text and each time it will add one marshmallow until 5, printing 5 too. Because it is incrementing before it prints.
marshmallows = 0
while marshmallows < 5:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")

# Task 2: 
# Now it is going to print 0, 1, 2, 3 and 4 marshmallow, that happens because we changed the order of actions in the loop, so first it compares, print and next add one marshmallow
# This makes the first print statement to print 0 marshmallows and lastly: 4 
marshmallows = 0
while marshmallows < 5:
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    marshmallows += 1

# Task 3:
marshmallows = 1
while marshmallows<10:
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    marshmallows += 1 #In this case, we are going to start adding 1 marshmallow but at the end we are going to add just 9, since the incrementation is placed at the end. 
    
marshmallows = 0
while marshmallows<10:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.") #In this case, we are going to start defining marshmallow as 0, we are adding 1 marshmallow at the beginning of the while loop, and at the end we are going to add 10, since the incrementation is placed at the beginning. 
     
print(DIVIDER)
print(GREETING)
print(DIVIDER)  
# 5. 

# Task 1:
start=0
while True:
    if start<5:
        print("This is an infinite loop")
        start+=1
    else:
        break
    
# The role in this case is to print five times "This is an infinite loop", but it is usually used to find items with specifical attributes iterating in all the items on a list, or repeat an action until something happens
# the break statement is usefull because it prevents to crash your computer in case that the conditional is never false and also are usefull to end the loop in case that the condition gets false.


# Task 2: Conditional Exit
start=0
while start<5:
    print("this is not an infinity loop")
    start+=1
# The condition makes the loop start and end, or it can do that the loop never starts, in case that the condition before the loop starts was true the loop would cheek and if the condition is true nothing is going to happen

# Task 3:
tap=5
top=-8
while tap!=top and top<0:
    
    print(f"different values: {tap} and {top}")
    tap-=1
else:
    print(f"here is it same values: {tap} and {top}")

# Combining different conditions in a single while loop allows us to use multiple varaible values using strings, integerers and different data type,
# allowing us to create complex loops that are more flexible, that also makes the code complex is the variety of conditionals that we can add.

print(DIVIDER)
print(GREETING)
print(DIVIDER)  
# 6.

# Task 1:
numbers = [0, 1, 2, 3, 4, 5, 6, 7,8]
i = 0

while i < len(numbers):
    if numbers[i] != 6:
        print(f"Value {numbers[i]} is not six.")
        i += 1
    else:
        print("Value six found!")
        break
else:
    print("Value six not found in the list.")

# Task 2: 
#in this case if we dont use the break it would continues printing the hour, until we stop it manually.
import time
act_time = time.localtime()
act_second = act_time.tm_sec
notloopsec = act_time.tm_sec +1
while True:
    act_time = time.localtime()
    act_hour = act_time.tm_hour
    act_minute = act_time.tm_min
    act_second = act_time.tm_sec
    print(f"the hour is {act_hour}:{act_minute}:{act_time.tm_sec}")
    time.sleep(1)
    if notloopsec== act_time.tm_sec:
        print("here is the hour and minute!")
        break

# Task 3:
# the utility of continue statement is to ignore some values that we dont want to print for example, or to extract other values, use the continue is useful to continue iterating without leave from the loop
numbers=[0,1,2,3,4,5,6,7,8,9,10]
i=0
while i < len(numbers):
    if numbers[i] %2==0:
        i +=1
        continue
    else:
        print(numbers[i])
        i+=1
    
# Task 4: 
x = 0
while x<3:
    x+=1
    pass

#the pass statement can be usefull when we are planning the structure of our program, also it is helpful to avoid errors in our code until we have it competely done, in this case we need to increment the value of x in the future.


print(DIVIDER)
print(GREETING)
print(DIVIDER)  
# 7. Python's Random Game Night

# Task 1: 
import random

count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
dict_roll ={
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0    
}

for i in range(10):
    dice_roll = random.randint(1, 6)
    count[dice_roll] += 1
    print("You rolled a " + str(dice_roll))
    if dice_roll==1:
        dict_roll["1"]+=1
    elif dice_roll==2:
        dict_roll["2"]+=1
    elif dice_roll==3:
        dict_roll["3"]+=1
    elif dice_roll==4:
        dict_roll["4"]+=1
    elif dice_roll==5:
        dict_roll["5"]+=1
    else:
        dict_roll["6"]+=1

        
for number, frequency in count.items():
    print(f"Number {number} was rolled {frequency} times.")
    
 
# Task 2: 
list1=[1,2,3,4,5,6]
choice = random.choice(list1)

guess = input("Choice a number between 1 and 6: ")
if guess == choice:
    print("You guessed correctly! ")
else:
    print("Good luck next time! ")

# Task 3:
cards = ["J", "Q", "K"]

random.shuffle(cards)
print(f"These are the shuffled carts: {cards}")

print(DIVIDER)
print(GREETING)
print(DIVIDER)  
# 8. The Random Challenge Course

# Task 1:
choice = random.randint(1,6)
guess = input("Choice a number between 1 and 6: ")

while choice != guess:
    try:
        if int(guess) < choice:
            guess = input("Incorrect! Your number is too low, try again: ")
        elif int(guess) > choice:
            guess = input("Incorrect! Your number is too high, try again: ")
        if choice == int(guess):
            break
    
    except ValueError:
        guess = input("This is not a number, try again: ")
        
if choice == int(guess):
    print("You guessed the correct number!")


# Task 2:
answers = ["Use a jacket today", "It is raining outside", "Drink some water", "You should study more", "No more sweets for you", "Maybe you are good enough", "Kind of true", "Eat some vegetables, and maybe you are going to feel better"]
question = input("Ask me something, put 'Quit' to exit the program: ")

while question.lower() != "quit":
    print(f"This is my advice for you: {random.choice(answers)}")
    question = input("Ask me something, put 'Quit' to exit the program: ")

if question.lower() == "quit":
    print("Hope you have a better day with my advice! 😊")
    

# Task 3: 
deck = []

types=['Diamond', 'Heart', 'Spade', 'Clover']
numbers=['1','2','3','4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
for t in types:
    for n in numbers:
        deck.append([t,n])

choice = random.choice(deck)

guess = input('Guess the card by type or number: ').lower()

if guess == choice[0].lower():
    print('Great, you found the type!')
elif guess == choice[1]:
    print('Great, you found the number!')
else:
    print('Wrong! 😒')
    
print(DIVIDER)
print(GREETING)
print(DIVIDER)  
# 9. Looping Lists - The Rhythm of Repetition

# Task 1: 
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
track_number = 1

for genre in genres:
    print(f"Track {track_number}: Now playing {genre}")
    track_number += 1
    
# Task 2: 
track_number = 1
genre = random.choice(genres)

while genre != 'Jazz':
    print(f"Track {track_number}: Now playing {genre}")
    track_number += 1
    genre = random.choice(genres)

if genre == 'Jazz':
    print('Playing good music 😎')



# Task 3:
unsuitable_genre = 'Classical'

for i in range(len(genres)):
    if genres[i] == unsuitable_genre:
        continue
    print(f"Track is {i + 1}: {genres[i]} - Light show is on!")


print(DIVIDER)
print(GREETING)
print(DIVIDER)  
# 10. Advanced Looping Techniques

# Task 1:
selected = genres[1:4]  

for genre in selected:
    print("Selective play: " + genre)
    
# Task 2: 
music_genres = [genre + " Music" for genre in genres]
print(music_genres)

# Task 3:
for number in range(10, 0, -1):
    time.sleep(0.3)
    print(f"Count: {number} - The beat drops now!")

print(DIVIDER)  
print('Have a great day!!')