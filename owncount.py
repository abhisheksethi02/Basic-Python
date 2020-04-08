yo="myself Shubham Kumar"
c=0
x=input("what you want to search: ")
x=str(x)
for i in yo:
    if(i==x):
        c=c+1
if(yo.count(x)==c):
    print("Yes")
else:
    print("No")
