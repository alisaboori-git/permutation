import math


text=input('type your text: ')
text=text.replace(' ','')
encoded_text=''
key=input('enter your key: ')
key_as_array=list(key)
key_as_array.sort()
text_with_z=text+(len(key)-(len(text)%len(key)))*'z'
order=[]

for i in key_as_array:
    order.append(key.find(i))
    key=key.replace(i,'@',1)
    

def slice_(text,key):
    start=0
    temp_array_colloction=[]    
    for i in range(math.floor(len(text)/len(key))+1):
        temp_array_colloction.append(text_with_z[start:(start+len(key))])
        start+=len(key)
    return temp_array_colloction

temp=slice_(text,key)



for i in order:
    for j in range(len(temp)):
        encoded_text+=temp[j][i]

print(order,encoded_text)