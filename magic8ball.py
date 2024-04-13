# Magic 8-Ball
# The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.
# 
# Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.
import random

name = "Jon Jon"
question = "Will I find a better job in 2024?"
# question = ""
answer = ""
random_number = random.randint(1,10)
# print(random_number)

if question != "": # Make sure we have a question to answer
    # Control flow 
    if random_number == 1:
        answer = "Yes - definitely"
    elif random_number == 2:
        answer = "It is decidely so"
    elif random_number == 3:
        answer = "Without a doubt"
    elif random_number == 4:
        answer = "Reply hazy, try again"
    elif random_number == 5:
        answer = "Ask again later"
    elif random_number == 6:
        answer = "Better not tell you now"
    elif random_number == 7:
        answer = "My sources say no"
    elif random_number == 8:
        answer = "Outlook not so good"
    elif random_number == 9:
        answer = "Yeahhhhhh, no"
    elif random_number == 10:
        answer = "Very doubtful"
    else:
        answer = "Oops! Error!"

    # Display
    if name == "":
        print(f"Question: {question}")
    else:
        print(f"{name} asks: {question}")

    print(f"Magic 8-Ball's answer: {answer}")

else:
    print("The fabric of reality is at risk!")
    print("I can't provide an answer if you don't ask a question.")