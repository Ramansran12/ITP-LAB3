#Ramandeep Singh
#22076254

a = {}
option = 0
#printing the options
print("WELCOME TO THE DEEP SHOPPING SITE ")
print("1. Add product to the cart")
print("2. Search the product")
print("3. Delete the product from the cart")
print("4. Quit")

while option != 4:
  #taking input from users
    option = int(input("Enter your option: "))
     # adding items into the cart
    if option == 1:
        t = int(input("Enter the number of items: "))

        j = 0
        while (j<t):
            if (t < 5):
                x = input("Enter an item: ")
                y = input("Enter brand name: ")
              #updating items
                a.update({x: y})
                print("You added following items")
              
            else:
                print("Cart is full")
                break
            j += 1
       # for searching an item
    elif option == 2:
        x = input("Enter the item you want to search : ")
        if x in a:
            print(x + ":" + a[x])
        else:
            print("Not found")

        #for delete an item
    elif option == 3:
        x = input("Enter item: ")
        if x in a:
            a.pop(x)
            print("item deleted successfully")
        else:
            print("Not found")
     #quiting from site
    elif option == 4:
        print("Thank you for shopping ")

    else:
      print("wrong option entered")

    print(a)