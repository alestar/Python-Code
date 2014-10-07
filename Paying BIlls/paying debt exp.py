def paying_bisection(balance,annualInterestRate):

    monthlyInterestRate = annualInterestRate/12
    lo = balance/12.0
    hi = (balance * (1+monthlyInterestRate)**12)/12.0
    newbalance = balance
    while True:
        newbalance = balance
        guess = (hi + lo)/2

        for count in range (1,13):
            interest = (newbalance-guess) * monthlyInterestRate
            newbalance += interest - guess

        if newbalance >= 0:
            lo=guess
        if newbalance < 0:
            hi=guess
        if (hi-lo<0.005):    
            break
    print round(guess,2)
