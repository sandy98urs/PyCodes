n1=int(input("Enter the number 1\n"))
n2=int(input("Enter the number 2\n"))
c=n1*n2
while n1 != n2:
    if n1 > n2:
        n1 = n1-n2
    else:
        n2 = n2-n1

print("hcf is:", n1)
print("lcm is:", c/n1)