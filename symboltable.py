s = list(input().split(" "))
print("generating the symbol table")
print("name\tsize\t          address")
for i in s:
    if(i.isdigit()):
        print(i,"\tnumber\t        ",id(i))
    if(i[0].isalpha()):
        print(i,"\tidentifier\t",id(i))
    else:
        if(i=='+' or i=='-' or i=='*' or i=='/' or i=='^'):
            print(i,"\toperator\t",id(i))
print("the end")
            