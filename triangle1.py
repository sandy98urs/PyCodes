def tri(a,b,c):
    if (a == b and a == c):
        print("Equilateral triangle\n")
    elif (a == b or a == c or b == c):
        print("isocelus triangle\n")
    else:
        print("scalene\n")

a=float(input("Enter the length of side 1:\n"))
b=float(input("Enter the length of side 2:\n"))
c=float(input("Enter the length of side 3:\n"))

tri(a,b,c)
