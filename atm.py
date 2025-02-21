from datetime import datetime
exit=True
inserted=False
balance=20000
actual_pin=None
blocked=False
attempts=0
transactions = []
while True:
    if not inserted:
        print('Welcome to SBI')
        print("Enter the ATM card")
        x=int(input("1 for yes,2 for no:"))
        if x==1:
            inserted=True
            if blocked:
                print('Your ATM card has been Blocked.\nContact your Branch Manager to unblock')
                inserted =False
                continue
            if actual_pin==None:
                actual_pin=int(input("Set your PIN:"))
            print("Enter the PIN")
            pin=int(input())
            if pin ==actual_pin:
                print(
                    """
        1.Deposit
        2.Withdrawal
        3.Mini statement
        4.PIN change
        """
                    )
                option =int(input("Select one of the option above"))
                if option==1:
                    print("Deposit")
                    amount=int(input("Enter the amount:"))
                    if amount%100==0:
                        balance=balance+amount
                        transactions.append(amount)
                        print("Cash has been accepted")
                        print("Available balance = ",balance)
                    else:
                        print("Feed only multiples of hundred")
                if option==2:
                    print("Withdrawal")
                    amount=int(input("Enter the amount:"))
                    if amount<balance:
                        if amount%100==0:
                            balance-=amount
                            transactions.append(-amount)
                            print("Take the cash")
                            print("Available balance = ",balance)
                        else:
                            print("Enter only multiples of hundred")
                    else:
                        print("Insufficiant Balance")
                if option==3:
                    datetim = datetime.now()
                    date = datetim.strftime('%d-%m-%Y')
                    time = datetim.strftime('%I:%M %p')
                    print(
                        f"""
                    State Bank of India
Date: {date}                          Time: {time}

Last Transactions: """)
                    for transaction in transactions:
                        print(f"""                    {transactions}""")
                       
                    print(f"""                                      
Available Balance                    {balance}

""" 
                    )      
                if option==4:
                    actual_pin=int(input("Enter New PIN"))
                   
                    
                     
            else:
                print("Invalid PIN")
                attempts +=1
                if attempts >= 3:
                    blocked=True
    else:
        inserted =False
        print("Please remove the card")