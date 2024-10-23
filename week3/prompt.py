string=input("enter the sentence:")
count=0
for item in string:
    count+=item.lower().count('a')
print("print number of times 'a' appears in:",count)
         
