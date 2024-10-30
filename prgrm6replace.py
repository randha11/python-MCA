str=input("enter a string:")
print("the original string is:",str)
k="$"
new_str=str.replace(str[0],k).replace(k,str[0],1)
print("replaced string",new_str)
