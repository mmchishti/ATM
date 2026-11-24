balance = float(input("Enter your initial balance: "))

x = ("a,b c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z")

if balance == x:
    print("Enter valid balance value")

while True:
    print("\n--- Bank Account Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Please select an option from the menu (1-4): ")
   
    if choice == "1":
      amount =  float(input("Enter your deposit value:"))
      balance += amount
      print("Your new balance is:", balance)

      if amount <= 0:
        print("Enter valid deposit value")
      else:
        print("Deposit Sucessfully")
    elif choice == "2":
        amount = float(input("Enter your withdraw value:"))
        if amount <= 0:
         print("Enter valid withdraw value")
        elif amount > balance:
          print("Insufficient funds")
        else:
           balance -= amount
           print("Withdraw Sucessfully")
           print("Your new balance is:", balance)
    elif choice == "3":
        print("Your current balance is:", balance)
    elif choice == "4":
        print("Thank you for using our banking system")
        break
    else:
        print("Invalid option. Please select a valid option from the menu.")

