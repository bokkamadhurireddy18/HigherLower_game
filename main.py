from game_data import data
import random
from art import logo, vs
print(logo)
score =-1

def higher_lower(a, b):
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
  print(vs)
  print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
  choice = input("Who has more followers? Type 'A' or 'B': ")
  if (a['follower_count']>b['follower_count'] and choice=="A"):
    print("Correct!")
    return True
  elif (a['follower_count']<b['follower_count'] and choice=="B"):
    print("Correct!")
    return True
  else:
    print("You Lost!")
    print(f"Your total Score is: {score}")
    return False
  
a= random.choice(data)
won= True
while won:
  b= random.choice(data)
  # to regenerate choice if a and b are same becuse cannot compare
  while (b==a):
    b= random.choice(data)
  score+=1
  print(f"Your total Score is: {score}")
  won= higher_lower(a, b)
  a=b #important because we are using option B in the game as option A in next game
  