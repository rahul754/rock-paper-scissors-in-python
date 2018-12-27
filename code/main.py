##Rock Paper Scissors Game

import random
print("""Winning Rules:  \n
	  "Rock vs Paper => paper wins" \n
	  "Rock vs Scissor => Rock wins" \n
	  "Paper vs Scissor => Scissor wins""")
	 
#Step 1 : conditions for the user

while True:
	print("Enter choice 1: Rock,2: Paper,3: Scissor")
	user_choice=int(input("User Turn: "))
	
	while user_choice>3 or user_choice<1:
		user_choice=int(input("Enter Valid Input : "))
	
	if user_choice==1:
		user_choice_name="Rock"
	elif user_choice==2:
		user_choice_name="Paper"
	else:
		user_choice_name="Scissor"
		
	print("user's choice is: "+user_choice_name)
	print("\nit's computer's Turn")
	
# Step 2 : Conditions for the computer

comp__choice=random.randint(1,3)
while comp_choice==user_choice:
	comp_choice=random.randint(1,3)
if comp_choice==1:
	comp_choice_name="Rock"
elif comp_choice==2:
	comp_choice_name="Paper"
else:
	comp_choice_name="Scissor"
	
print("Computer's choice is: "+comp_choice_name)
print(user_choice_name+ " v/s "+ comp_choice_name)


# Step 3 : Condition  of winning !!!

if ((user_choice==1 and comp__choice==2) or
    (user_choice==3 and comp_choice==1)):
	print("Paper win=> ",end='')
	result='paper'
elif((user_choice==1 and comp__choice==3) or
     (user_choice==3 and comp__choice==1)):
	 print("Rock wins=>",end="")
	 result="rock"
else:
	print("scissor wins=>",end='')
	result='scissor'
	
# Step 4: Printing the winner

if result==user_choice_name:
	print("** user wins **>")
else:
	print("<** Computer Wins **>")

print("Do you want to play again ? (Y/N)")
ans=input()


if ans=='n' or ans=='N':
	break

print("\n Thanks for playing")