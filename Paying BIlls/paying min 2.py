def paying_min(balance,annualInterestRate,monthlyPaymentRate):

updated_balance=balance
monthly_interest_rate= annualInterestRate/ 12.0
i=1
total_amount=0
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
