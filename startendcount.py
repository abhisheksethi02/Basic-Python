sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
same_letter_count=0
z=0
# Write your code here.
y=sentence[0]
for i in sentence[1:]:
    while i!=" ":
        if(i==y):
            same_letter_count+=1



print(same_letter_count)
