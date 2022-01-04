
import sys
import random 

print("Welcome to McDonald\'s!")
print("Can I Take Your Order?")
order=input()

McFlurry="ice cream"

if order == "McFlurry": 
 print("Our ice cream machine is broken!")
 sys.exit()
  

print("Great! Come pick it up in 15 minutes!")
print("15 mins later...")
print("Your order is ready!")
print("Come pick it up at the door!!")


picked_up = input("Enter true to confirm the pick up, enter false to deny. :")

if picked_up == "true":
  print("Have a great day!")
elif picked_up == "false":
  print("We'll check with our team!")
else:
  print("Hmm, that doesn't sound right. Try to order again.")
  sys.exit()