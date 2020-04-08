largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":break
    try:
        n=int(num)
        print(n)
        if(smallest is None):
            smallest=n
        elif(n>smallest):
            x=smallest
            if(largest is None):
                largest=n
            elif(n<largest):
                y=largest
        else:
            x=n
            smallest=x
    except:
        print("Invalid")
print("Maximum is",y)
print("Minimum is",x)
