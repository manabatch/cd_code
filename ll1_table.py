E='@'
is_terminal = lambda x: not x.isupper()
prods={}
first_set={}
follow_set={}
ll1_set={}

def first(head: str,prods : dict):
    if is_terminal(prods[head][0][0]):
        ret = [p[0][0] for p in prods[head] if is_terminal(p[0][0])]
        for p in prods[head]:
            if E in p:
                ret.append(E)
        return ret
    return first(prods[head][0][0],prods)

def follow(head:str,prods:dict):
    global E,first_set,follow_set
    res=[]
    if head=='E':
        res.append('$')
        for p in prods.keys():
            x = prods[p]
            for item in x:
                if len(item)==3:
                    if item[1]=='E':
                        if is_terminal(item[2]):
                            res.append(item[2])
        return list(set(res))
    else:
        for p in prods.keys():
            x = prods[p]
            for item in x:
                if len(item)==2:
                    if item[1]==head:
                        res =res+follow_set[p]
                elif len(item)==3:
                    flag=0
                    for y in x:
                        if y[0]=='@':
                            flag=-1
                            break
                    if flag==0:
                        if item[1]==head:
                            res = res + first_set[item[2]]
                    else:
                        if item[1]==head:
                            temp = first_set[item[2]].copy()
                            while '@' in temp:
                                temp.remove('@')
                            res = res + temp
                            res = res + follow_set[p]
        return list(set(res))

def ll1(prods:dict):
    global E,first_set,follow_set,ll1_set
    temp_dict={}
    for x,y in prods.items():
        temp=[]
        for item in y:
            temp.append(''.join(item))
        temp_dict[x]=temp
    # print(temp_dict)
    for item in first_set.keys():
        res=[]
        x=first_set[item]
        for y in x:
            if y != '@':
                if y=='i' and y in temp_dict[item]:
                    res.append(y+' : '+item+'->'+y)
                else:
                    res.append(y+' : '+''+item+'->'+temp_dict[item][0])
            else:
                liste = follow_set[item]
                for z in liste:
                    res.append(z+' : '+item+'->'+'@')
        ll1_set[item]=res


def main():
    global prods,first_set,follow_set
    p=int(input("Enter number of productions:"))
    for i in range(1,p+1):
        buf=input(f"{i} :")
        head,body = [x.strip() for x in buf.split("->")]
        body= [[y for y in x.strip().split(" ")] for x in body.split("|")]
        prods[head] = body
    for (k,_) in prods.items():
        first_set[k] = list(set(first(k,prods)))
    for (k,_) in prods.items():
        follow_set[k] = list(set(follow(k,prods)))
    ll1(prods)

    # print(prods)
    print(first_set)
    print(follow_set)
    print(ll1_set)

if __name__=="__main__":
    main()
