def paying_debt(balance,annualInterestRate):
    '''
    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal
    
    ----------------------------------------------MATH----------------------------------------------------------
    Monthly interest rate= (Annual interest rate) / 12.0
    
    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

    ------------------------------------------------EXPLICATION-------------------------------------------------
    Given an initial balance, what code would compute the balance at the end of the year?
    Now imagine that we try our initial balance with a monthly payment of $10. If there is a balance remaining at the end of the year,
    how could we write code that would reset the balance to the initial balance, increase the payment by $10, and try again (using the same code!)
    to compute the balance at the end of the year, to see if this new payment value is large enough.
    I'm still confused!
    A good way to implement this problem will be to use a loop structure. You may want to refresh your understanding of while loops.
    Think hard about how the program will know when it has found a good minimum monthly payment value - when a good value is found, the loop can terminate.
    Be careful - you don't want to overwrite the original value of balance. You'll need to save that value somehow for later reference!
    '''
    minimum_monthly_payment=0
    monthly_interest_rate= annualInterestRate/ 12.0  
    end= False
    while not end:
        update_balance= balance
        minimum_monthly_payment +=10
        i=1
        for i in range(1,13):
            
            prev_balance=round(update_balance,2)
            monthly_unpaid_balance= prev_balance - minimum_monthly_payment
            update_balance= monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)          
            '''
            print('Month: ' + str(i))
            print('Prev_balance: ' + str(prev_balance))
            print('Minimum_monthly_payment: ' + str(round(minimum_monthly_payment,2) ) )
            print('Monthly_unpaid_balance: ' + str(round(monthly_unpaid_balance,2) ) )
            print('Updated_balance: ' + str(round(update_balance,2)))
            print('Remaining balance: ' + str(round(update_balance,2)))
            '''
            i+=1
      
        if update_balance < 0:
            end= True
            
    print(' Lowest Payment: ' + str ( round(minimum_monthly_payment,2) ) )

