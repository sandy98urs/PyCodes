import math


a=float(input("Enter coefficient a:"))
b=float(input("Enter coefficient b:"))
c=float(input("Enter coefficient c:"))

disc = (b*b)-(4*a*c)

if disc > 0:
    root1 = (-b + math.sqrt(disc)) / (2 * a)
    root2 = (-b - math.sqrt(disc))/ (2 * a)
    print("Roots are real\n",root1,"\t",root2)
elif disc < 0:
    root1 = (-b)/(2*a)
    root2 = math.sqrt(-disc)/(2*a)
    print("Roots are imaginary \n",root1,"+i",root2,"\t",root1,"-i",root2)
elif disc == 0:
    root = (-b)/(2*a)
    print("Roots are\n",root,"\t",root)


