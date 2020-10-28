def Bsearch(AR,ITEM):
    beg=0
    last=len(AR)-1
    while(beg<=last):
        mid=(beg+last)//2
        if(ITEM==AR[mid]):
            return mid
        elif(ITEM>AR[mid]):
            beg=mid+1
        else:
            last=mid-1
    else:
        return -1

AR=['apple','orange','banana','pear','raspberry','peach','plum']
ITEM=(input("\nEnter Element to be searched for..."))
index=Bsearch(AR,ITEM)
if index>=0:
    print("\nELement found at index:",index,",Position:",(index+1))
else:
    print("\nSorry!! Given element could not be found.\n")

# If there are 10 million fruits in the list and the user wants to know if 'apple' is in the fruits list, 
# fortunately, apple happens to be the first fruit in the list. Now ask yourself, after the code finds 
# apple early on in the list, will it continue to search through the remain items in the list or it 
# will stop there and print out 'There'. Think about it, find out what your code does and let me know.


