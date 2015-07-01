#printing the repeated characters in a string
string=raw_input("enter the string")
count={}
for char in string:
 if char in count.keys():
    count[char] +=1
 else:
    count[char] =1
      
print (count)
      
