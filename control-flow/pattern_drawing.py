#Prompting the user to input the pattern size
size = int(input("Enter the size of the pattern: "))

#Storing the original size to use in the loop
size1 = size

#While loop to iterate each row
while size > 0:
    #For loop for printing asterisks
    for i in range(0,size1):
        print("*", end="")

    #print a new line
    print()

    #Decrease the size to move to next row
    size-=1

