def paying_min(balance,annualInterestRate,monthlyPaymentRate):
    '''
    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

    monthlyPaymentRate - minimum monthly payment rate as a decimal
    --------------------------------------------------------------------------------------------------------
    Monthly interest rate= (Annual interest rate) / 12.0
    
    Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    
    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance

    --------------------------------------------------------------------------------------------------------
    For each month:
    - Compute the monthly payment, based on the previous month’s balance.
    - Update the outstanding balance by removing the payment, then charging interest on the result.
    - Output the month, the minimum monthly payment and the remaining balance.
    - Keep track of the total amount of paid over all the past months so far.
    - Print out the result statement with the total amount paid and the remaining balance.
     round(2.675, 2)
    '''
     
    prev_balance= 0
    updated_balance=balance
    monthly_interest_rate= annualInterestRate/ 12.0
    minimum_monthly_payment=0
    monthly_unpaid_balance=0    
    total_amount=0
    i=1  
    for i in range(1,13):
        
        prev_balance=updated_balance
        minimum_monthly_payment= monthlyPaymentRate * prev_balance
        monthly_unpaid_balance= prev_balance - minimum_monthly_payment
        updated_balance= monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        
        print('Month: ' + str(i))
        print('Minimum monthly payment: ' + str(round(minimum_monthly_payment,2)))
        print('Remaining balance: ' + str(round(updated_balance,2)))


        total_amount += minimum_monthly_payment
        i+=1
    print('Total paid: ' + str(round(total_amount,2)))
    print('Remaining balance: ' + str(round(updated_balance,2)))
