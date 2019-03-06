
try:
    F=float(input("Enter the temperature in Fahrenheit: \n"))

    C=(F - 32) * 5/9

    print("Temperature in degree:",C,"deg\n")
except:
    print("Error")
    exit(0)