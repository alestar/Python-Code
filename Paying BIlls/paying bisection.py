def paying_bisection(balance,annualInterestRate):
    '''
    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal
    
    ----------------------------------------------MATH----------------------------------------------------------
    Monthly interest rate= (Annual interest rate) / 12.0
    
    Monthly payment lower bound = Balance / 12
    
    Monthly payment upper bound = (Balance x (1 + Monthly interest rate)^12) / 12.0

    ------------------------------------------------EXPLICATION-------------------------------------------------
    To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year.
    What is a reasonable lower bound for this payment value? $0 is the obvious anwer, but you can do better than that.
    If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month.
    One-twelfth of the original balance is a good lower bound.

    What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year.
    What we ultimately pay must be greater than what we would've paid in monthly installments,
    because the interest was compounded on the balance we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance,
    after having its interest compounded monthly for an entire year.
    '''
    monthly_interest_rate= annualInterestRate/ 12.0
    
    low = balance / 12.0
    
    hi = (balance * (1 + monthly_interest_rate)**12) / 12.0
    
    #minimum_monthly_payment= (monthly_payment_upper_bound + monthly_payment_lower_bound)/2.0
    minimum_monthly_payment= (low + hi)/2.0   
    #epsilon = 0.01
    #update_balance= balance
    #end= False
    while True:
    #while not end:
    #while abs(minimum_monthly_payment *12 - (balance * (1 + monthly_interest_rate)**12)) >= epsilon:

        #if minimum_monthly_payment < update_balance:
        #if minimum_monthly_payment *12 < (balance * (1 + monthly_interest_rate)**12):
        #low= minimum_monthly_payment
        #else:
        #hi= minimum_monthly_payment
        update_balance= balance
        minimum_monthly_payment= (low + hi)/2.0     
        for i in range(1,13):
            monthly_unpaid_balance= update_balance - minimum_monthly_payment
            update_balance= monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)

            '''
            if newbalance >= 0:
                lo=guess
            if newbalance < 0:
                hi=guess
            if (hi-lo<0.005):    
                break
            '''

           # if   update_balance >=0 and update_balance <=1:
            if (abs(hi-low)<0.005):
                break
            elif update_balance >= 0:
                low= minimum_monthly_payment
            elif update_balance < 0:
                hi= minimum_monthly_payment
            
    print(' Lowest Payment: ' + str ( round(minimum_monthly_payment,2) ) )
