import math


text=input('type your text: ')
text=text.replace(' ','')
key=input('enter your key: ')
key_as_array=list(key)
key_as_array.sort()
sorted_key_str=''.join(key_as_array)
decoded_text=''

order=[]
for i in key:
    order.append(sorted_key_str.find(i))
    sorted_key_str=sorted_key_str.replace(i,'@',1)

def slice_(text,key):
    start=0
    temp_array_colloction=[]    
    for i in range(len(key)):
        temp_array_colloction.append(text[start:(start+(math.floor(len(text)/len(key))))])
        start+=(math.floor(len(text)/len(key)))
    return temp_array_colloction

temp=slice_(text,key)

ordered_list=[]
for i in order:
    ordered_list.append(temp[i])


for j in range(math.floor(len(text)/len(key))):
    for i in range(len(ordered_list)):
        decoded_text+=ordered_list[i][j]
# for i in order:
#     for j in range(len(temp)):
#         decoded_text+=temp[j][i]

print(order,decoded_text)