def display_menu():
    print('Shopping List Manager')
    print('1. Add Item')
    print('2. Remove Item')
    print('3. View List')
    print('4. Exit')

def main():
    shopping_list = []

    #Loop
    while True:
        display_menu()
        choice = input('Enter your choice: ')

        if choice == '1': #Adding to list
            add = input('Enter the item to add: ')
            shopping_list.append(add)

        elif choice == '2': #Removing unwanted item
            remove = input('Type the item you want to remove: ')
            if remove in shopping_list:
                shopping_list.remove(remove)
            else:
                print('Item not found')

        elif choice == '3': #Displaying each item of the shopping list
            for i in shopping_list:
                print(i)

        elif choice == '4': #To exit the loop by displaying goodbye
            print('Goodbye!')
            break

        else: #To check invalid choices
            print('Invalid choice. Please try again.')

#To execute directly and not when imported as a module
if __name__ == "__main__":
    main()
