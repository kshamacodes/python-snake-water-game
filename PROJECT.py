
import random as r
#1:SNAKE
#2:WATER
#3:GUN
while True:
     op=r.randint(1,3)
     if op == 1:
         oc="snake"
     elif op == 2:
         oc="water"
     else:
         oc="gun"
     choose=input("your choice:")
     choice=choose.strip().lower()
     sn="snake"
     wt="water"
     gn="gun"
     if choice not in ["snake","water","gun"]: 
         print("invalid choice")
         print("choose any one from snake,water,gun")
         continue
     elif choice == "snake" and op == 1:
         print("It's a tie")
     elif choice == "snake" and op == 2:
         print("You win")
     elif choice == "snake" and op == 3:
         print("You lose")
     elif choice == "water" and op == 1:
         print("You lose")
     elif choice == "water" and op == 2:
         print("It's a tie")
     elif choice == "water" and op == 3:
         print("You win")
     elif choice == "gun" and op == 1:
         print("You win")
     elif choice == "gun" and op == 2:
         print("You lose")
     elif choice == "gun" and op == 3:
         print("It's a tie")
     print("opposite team choose:",oc)
     again=input("want to continue more?:").strip().lower()
     if again.lower() not in ["yes","no"]:
        print ("invailid answer (yes/no)")
     if again =="no":
         break 
    