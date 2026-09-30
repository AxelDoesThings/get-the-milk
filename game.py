# ✏️ Replace EVERYTHING in this file with your own game from OnlineGDB.
#    (Click the pencil icon, select all, paste, then Commit changes.)
#Go Buy The Milk!

def ask(prompt, options):
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print(f" Pick one of: {', '.join(options)}")

state = "walking" #walking item buying_milk greedy
money = 8
stop = 0
bought_milk = None

print("Your Mom gave you $8 to go buy milk from the store. She said you could still buy yourself something at the store with the change.")

while bought_milk == None:
    if state == "walking":
        if stop == 0:
            print("At the store, as you walk towards the milk isle, you pass the candy isle. Do you buy a candy bar worth $2")
        elif stop == 2:
            print("Further down you walk past the refridgerator isle and spot an Arizona can for a dollar.")
        elif stop == 4:
            print("Just before you get to the milk you spot a large bag of Takis for $5")
        state = "item"
        stop += 1
    elif state == "item":
        state = "walking"
        if stop == 1:
            snack = "Candy Bar"
            cost = 2
        elif stop == 3:
            snack = "Arizona"
            cost = 1
        elif stop == 5:
            snack = "Takis"
            cost = 5
            state = "milk"
        if ask(f" Do you [b]uy the {snack} for ${cost} or [l]eave it. ", ["b" , "l"]) == "b":
            money -= cost
            print(f" You bought the {snack}!")
        stop += 1
    elif state == "milk":
        if money >= 5:
            print("You had enough money to but the milk for $5")
            bought_milk = True
            money -= 5
        else:
            print("You couldn't afford the milk, I wonder why?")
            bought_milk = False
        state = "walking"
    print(f"\n[STATE: {state.upper()} | ${money}]")
    
if bought_milk == False:
    print("Did you forget why you were here? \n Bad Ending")
elif money == 0:
    print("You bought the milk! Just hope Mom doesn't ask for any change. \n Snack Ending")
elif money == 3:
    print("You bought the milk! and you were able to give all the change back to mom. \n Responsible Ending")
else:
    print(f"You bought the milk your Mom asked for, some snack(s) for yourself, and with ${money} to spare.  \n Normal Ending")
