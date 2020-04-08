mail=open('C:\\Users\\dell\\Desktop\\email.txt')
for wrd in mail:
    if wrd.startswith('From'):
        print(wrd)
