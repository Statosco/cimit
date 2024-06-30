userName = input("what is your name? ")

print(f"hello {userName} and welcome to nobody's funds! where we like your money, "\
       "before we begin we would like you to fill up a form for your loan")

print("1 year for 2.5% \n2 years for 3.5% \n3 years for 4.5% \n4 years for")

loanAmout = input("How much would you like: $")
noPayment = input("how long are you interested in repayment? ")
interst = input("what is your interest?: ? %")
loanInterest = interst / 100

mp = loanAmout * interst * (1 + loanInterest)  

