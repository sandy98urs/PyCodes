def compound_interest(P,T,R):
     print("compound interest is=",P*pow((1+R/100),T))

def simple_interest(P,T,R):
        print("Simple interest is=",((P*T*R)/100))


P=float(input("Enter the principle amount\n"))
T=float(input("Enter the Time period in years\n"))
R=float(input("Enter the rate\n"))

compound_interest(P,T,R)
simple_interest(P,T,R)
