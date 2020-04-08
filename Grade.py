score=input("Enter Score:")
try:
    sc=float(score)
except:
    print("Error")
    quit()
if(sc<0.6):
    print('F')
elif(sc<0.7):
    print('D')
elif(sc<0.8):
    print('C')
elif(sc<0.9):
    print('B')
elif(sc<1.0):
    print('A')
