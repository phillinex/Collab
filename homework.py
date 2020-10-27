a=['apple','orange','banana','pear','raspberry','peach','plum']
fruit=input("Enter name of the fruit:")
if fruit in a:    
    print("There")
else:
    print("Not there")

# If there are 10 million fruits in the list and the user wants to know if 'apple' is in the fruits list, 
# fortunately, apple happens to be the first fruit in the list. Now ask yourself, after the code finds 
# apple early on in the list, will it continue to search through the remain items in the list or it 
# will stop there and print out 'There'. Think about it, find out what your code does and let me know.