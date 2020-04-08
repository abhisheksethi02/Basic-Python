import re
line=open('C:\\Users\\dell\\Desktop\\email.txt')
for wrd in line:
    wrd=wrd.rstrip()
    if re.search("^From:\s+",wrd):
        print(wrd)
    y=re.findall('[0-9]',wrd)
    print(y)
