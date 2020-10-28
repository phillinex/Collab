
AR=['apple','orange','banana','pear','raspberry','peach','plum']
ITEM=(input("\nEnter Element to be searched for..."))

if any(ITEM == fruit for fruit in AR): 
    # Here we pick the items in AR one by one and compare with input, 
    # if any (first instance) is the same as input we take it as true 
    # because nothing after that can change the outcome
    print("Its There")
else:
    print("Not There")

