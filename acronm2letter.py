stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

sent_lst=sent.split()
acro1=[]
acro=''
for wrd in sent_lst:
    if wrd not in stopwords:
        acro1.append(wrd[0].upper()+wrd[1].upper())
acro=acro1.join(".")
