
"""
Challenge 
    We are going to make a "Shopping List" app. 
    Run the script to start using it.
    Put new things into the list one at a time
    Enter the word DONE - in all CAPS - to QUIT the program
    And once i quit, I want the app to show me everything thats on my list.
​
Hint 1
    Step 1: Make a list to hold onto our items.
    Step 2: Print out instructions on how to use the app
​
    Step 3: Ask for new items
    Step 4: Add new items to our list
    Step 5: Be able to quit the app
​
    Step 6: print out the list
"""

list1=[]
print("What should we pick at the store?""\n""enter 'DONE' to stop adding items")
while(True):
    str=input("Add item:")
    if(str=="DONE"):
        print("Here's your list")
        print(list1)
        break
    else:
        list1.append(str)
     